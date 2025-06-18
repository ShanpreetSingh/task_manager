from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telegram_username = models.CharField(max_length=100, blank=True, null=True)

class TelegramUser(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.chat_id})"