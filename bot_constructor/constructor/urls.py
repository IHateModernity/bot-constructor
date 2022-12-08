from django.urls import path, include
from .views import createnewbot, BotAddCommand, func

urlpatterns = [

    path('create-new-bot/', createnewbot, name='create-new-bot'),
    path('bot-add-command/', BotAddCommand.as_view(), name='bot-add-command'),
    path('', func, name='bots')
]