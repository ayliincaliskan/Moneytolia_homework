from datetime import date
from http.client import HTTPException
import json
from hashlib import md5
from django.conf import settings
import redis
from rest_framework import generics
from django.http import JsonResponse
from django.db.models import Count

from moneytolia_homework.accounts.models import APIKey
from moneytolia_homework.control.models import DailyLimit, ShortURL

# Redis connection
redis_client = redis.Redis(host='moneytolia_homework-redis-1', port=6379, db=0, decode_responses=True)

# URL shortening endpoint
class ShortenUrl(generics.GenericAPIView):
    def post(self, request):
        data = json.loads(request.body)
        url_request = data.get('url_request')
        api_key = request.headers.get('Api-Key')

        try:
            # Finding the user with API key
            api_key_obj = APIKey.objects.get(key=api_key)
            user = api_key_obj.user
        except APIKey.DoesNotExist:
            raise HTTPException(status_code=403, detail="Invalid API key")

        today = date.today()
        try:
            # User's daily quota control
            limit = DailyLimit.objects.get(user=user, date=today)
        except DailyLimit.DoesNotExist:
            limit = DailyLimit(user=user, date=today, url_count=0)
            limit.save()

        if limit.url_count >= 50:
            raise HTTPException(status_code=403, detail="Daily limit exceeded")
        # Quota increase
        limit.increment()
        # URL shortening algorithm (hashing)
        short_url = md5(url_request.encode()).hexdigest()[:6]
        # Save shortened URL to database
        ShortURL.objects.create(user=user, original_url=url_request, short_url=short_url)

        redis_client.set(short_url, url_request, ex=settings.REDIS_EXPIRATION_TIME)
        return JsonResponse({"short_url": short_url, "limit": limit.url_count})

# logic to find and redirect original_url from short_url
class Original(generics.GenericAPIView):
    def get(self, request):
        short_url = request.GET.get('short_url')
        # If available in Redis, return quickly
        original_url = redis_client.get(short_url)
        if original_url:
            return JsonResponse({"original_url": original_url})
        # If it is not available in Redis, get it from the database
        try:
            short_url_obj = ShortURL.objects.get(short_url=short_url)
            original_url = short_url_obj.original_url
        except ShortURL.DoesNotExist:
            raise HTTPException(status_code=404, detail="Short URL not found")
        # Save to Redis again
        redis_client.set(short_url, original_url, ex=settings.REDIS_EXPIRATION_TIME)
        return JsonResponse({"original_url": original_url})


class Analytics(generics.ListAPIView):
    def get(self, request):
        api_key = request.headers.get('Api-Key')
        try:
            api_key_obj = APIKey.objects.get(key=api_key)
            user = api_key_obj.user
        except APIKey.DoesNotExist:
            raise HTTPException(status_code=403, detail="Invalid API key")
        
        result = (
            ShortURL.objects
            .filter(user=user)
            .values('original_url', 'short_url')
            .annotate(click_count=Count('id'))
        )
        return JsonResponse(list(result), safe=False)
