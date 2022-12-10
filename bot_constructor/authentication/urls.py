from django.urls import path
from .views import authenticate_, profile
urlpatterns = [
    path('authentication',authenticate_,name='authentication'),
    path('profile/<str:pk>',profile,name='profile')
]