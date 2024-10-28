from django.contrib import admin

from moneytolia_homework.accounts.models import APIKey
from moneytolia_homework.control.models import DailyLimit, ShortURL


class ShortURLAdmin(admin.ModelAdmin):
    list_display = ("user", "original_url", "short_url")

class DailyLimitAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "url_count")