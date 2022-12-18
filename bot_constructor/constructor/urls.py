from django.urls import path, include
from .views import CreateNewBot, BotEdit, CommandDeleteView, BotAddCommand, BotList

urlpatterns = [
    path('bot/<str:pk>/', BotEdit.as_view(), name='bot-edit-page'),
    path('create-new-bot/', CreateNewBot.as_view(), name='create-new-bot'),
    path('bot-add-command/', BotAddCommand.as_view(), name='bot-add-command'),
    path('command-delete-page/<int:pk>/', CommandDeleteView.as_view(), name='command-delete-page'),
    path('', BotList.as_view(), name='bots')
]