from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Command(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    bot_name = models.CharField("Bot's name", max_length=30) # Будет вылазить выбор всех ботов пользователя

    type = models.CharField("Type", max_length=10) # Тип команды бота

    command = models.TextField('Command', max_length=255) # Команда которая будет писаться через слеш

    answer = models.BooleanField('Answer', default=False) # Ответ на эту команду

    creating_date = models.DateTimeField('Date of changing', null=True, auto_now=True) # Дата изменения бота (создания новой команды)


    def __str__(self):
        return self.command

    class Meta:
        verbose_name = 'Command'
        verbose_name_plural = 'Commands'
        ordering = ['creating_date']
