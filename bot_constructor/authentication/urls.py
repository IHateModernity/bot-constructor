from django.urls import path
from .views import authenticate_, ProfileView
from django.contrib.auth import views as authViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('authentication', authenticate_, name='authentication'),
    path('logout', authViews.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/<str:pk>', ProfileView.as_view(), name='profile')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)