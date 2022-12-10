from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField('Аватарка', blank=True)
    telegram = models.CharField('Телеграмм',blank=True,max_length=40)

    email = models.EmailField('Email', unique=True)

    def __str__(self):
        return self.username
