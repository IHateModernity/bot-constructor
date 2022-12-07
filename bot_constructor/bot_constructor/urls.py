"""bot_constructor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('constructor.urls')),


]

"""
    Объясняю, две привязки нужны для того чтоб у нас не было лишней хуйни site.com/user/register
    Вместо этого на выходе получим site.com/authentication где будут обе формы. Просьба к Тиму, НЕ создавай в своем приложении ссылку на домашнюю path('', func) 
    """