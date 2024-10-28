from rest_framework import serializers
from django.contrib.auth.models import User

from moneytolia_homework.accounts.models import APIKey
import random
import string


def generate_api_key():
    return "".join(random.choices(string.ascii_letters + string.digits, k=30))


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ['user', 'key']
    
    def create(self, validated_data):
        api = generate_api_key()
        api_key = APIKey.objects.create(**validated_data, key=api)
        return api_key