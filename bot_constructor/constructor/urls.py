from django.urls import path, include
from .views import CreateNewBot, BotAddCommand, BotList

urlpatterns = [

    path('create-new-bot/', CreateNewBot.as_view(), name='create-new-bot'),
    path('bot-add-command/', BotAddCommand.as_view(), name='bot-add-command'),
    path('', BotList.as_view(), name='bots')
]