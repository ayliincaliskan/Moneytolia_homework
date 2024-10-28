from django.http import JsonResponse

from moneytolia_homework.accounts.models import APIKey

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get('Api-Key')
        # The check was passed because there is no API key yet.
        if request.path == '/api/accounts/create-user/' and request.method == 'POST':
            return self.get_response(request)
        if request.path == '/api/accounts/create-api-key/' and request.method == 'POST':
            return self.get_response(request)
        
        if not api_key:
            return JsonResponse({'error': 'API key is missing'}, status=401)
        try:
            APIKey.objects.get(key=api_key)
        except APIKey.DoesNotExist:
            return JsonResponse({'error': 'Invalid API key'}, status=401)

        return self.get_response(request)