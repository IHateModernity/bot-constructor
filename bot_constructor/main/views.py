from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

def about(request):
    return render(request, 'main/about.html')

def index(request):
    """Функция для главной страницы"""
    return render(request, 'main/index.html')

