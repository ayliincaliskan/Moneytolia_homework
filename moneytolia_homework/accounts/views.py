from rest_framework import generics

from moneytolia_homework.accounts.serializers import UserSerializer, ApiKeySerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ApiKeyCreateView(generics.CreateAPIView):
    serializer_class = ApiKeySerializer

    