from django.forms import ModelForm
from .models import Command, Bot

class CreateNewBotForm(ModelForm):
    class Meta:
        model = Bot
        fields = ['bot_username', 'bot_token', ]


class CommandCreateForm(ModelForm):
    class Meta:
        model = Command
        fields = ['bot_name', 'bot_token', 'type', 'message', 'answer', ]
