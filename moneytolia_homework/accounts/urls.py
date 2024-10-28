from moneytolia_homework.accounts import views
from django.urls import path


urlpatterns = [
    path('create-user/', views.UserCreateView.as_view(), name='create-user'),
    path('create-api-key/', views.ApiKeyCreateView.as_view(), name='create-api-key'),
]