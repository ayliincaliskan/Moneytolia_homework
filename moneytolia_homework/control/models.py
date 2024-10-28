from datetime import date
from django.db import models
from django.contrib.auth.models import User

class ShortURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_url = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"
    
    
class DailyLimit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    url_count = models.IntegerField(default=0)

    def increment(self):
        self.url_count += 1
        self.save()