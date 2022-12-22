from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Bot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bot_username = models.CharField("Bot's username", max_length=30)
    bot_token = models.CharField("Bot's token", max_length=50)
    has_script = models.BooleanField('Has script?', default=False)
    script_path = models.CharField('Path', default='', max_length=70)

    def __str__(self):
        return self.bot_username


class Command(models.Model):
    bot_name = models.CharField('Name', max_length=30) # Будет вылазить выбор всех ботов пользователя
    bot_token = models.CharField('Token', default=None, max_length=30)
    type = models.CharField('Type', default='command', max_length=10) # Тип команды бота
    message = models.CharField('', default='Target message', max_length=10) # Команда которая будет писаться через слеш
    answer = models.TextField('Answer', max_length=255) # Ответ на эту команду
    creating_date = models.DateTimeField('Date of changing', null=True, auto_now=True) # Дата изменения бота (создания новой команды)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Command'
        verbose_name_plural = 'Commands'
        ordering = ['creating_date']