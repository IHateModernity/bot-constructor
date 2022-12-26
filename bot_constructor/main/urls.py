from django.urls import path, include
from .views import index, about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about,name='about'),
]