from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, '')

def index(request):
    """Функция для главной страницы"""
    return HttpResponse('Main')