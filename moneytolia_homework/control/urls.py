from moneytolia_homework.control import views
from django.urls import path


urlpatterns = [
    path('shorten-url/', views.ShortenUrl.as_view(), name='shorten-url'),
    path('original-url/', views.Original.as_view(), name='original-url'),
    path('analytics/', views.Analytics.as_view(), name='analytic'),
]