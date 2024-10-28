from django.db import models
from django.contrib.auth.models import User
import uuid

class APIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True, default=uuid.uuid4) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key