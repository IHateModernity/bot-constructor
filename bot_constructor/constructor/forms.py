from django.forms import ModelForm
from .models import Command


class CommandCreateForm(ModelForm):
    class Meta:
        model = Command
        fields = ['bot_name', 'type', 'command', 'answer', ]
