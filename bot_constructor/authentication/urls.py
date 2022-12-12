from django.urls import path
from .views import authenticate_, ProfileView
from django.contrib.auth import views as authViews

urlpatterns = [
    path('authentication', authenticate_, name='authentication'),
    path('logout', authViews.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/<str:pk>', ProfileView.as_view(), name='profile')
]