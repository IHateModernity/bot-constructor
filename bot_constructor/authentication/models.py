from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField('Email', unique=True)

    avatar = models.ImageField('Avatar', blank=True, upload_to=f'avatars/')
    telegram_id = models.CharField('Telegram id', blank=True, max_length=40)

    def __str__(self):
        return self.username
