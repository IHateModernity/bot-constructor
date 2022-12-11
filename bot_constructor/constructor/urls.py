from django.urls import path, include
from .views import CreateNewBot, BotAddCommand, func

urlpatterns = [

    path('create-new-bot/', CreateNewBot.as_view(), name='create-new-bot'),
    path('bot-add-command/', BotAddCommand.as_view(), name='bot-add-command'),
    path('', func, name='bots')
]