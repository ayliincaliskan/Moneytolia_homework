from django.contrib import admin


class APIKeyAdmin(admin.ModelAdmin):
    list_display = ("user", "key")