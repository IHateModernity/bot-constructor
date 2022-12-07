from django.urls import path, include
from .views import index, createnewbot, BotAddCommand

urlpatterns = [
    path('', index, name='home'),
    path('create-new-bot/', createnewbot, name='create-new-bot'),
    path('bot-add-command/', BotAddCommand, name='bot-add-command')
]