from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

import os
import sys
sys.path.append(os.path.join('../../'))

def about(request):
    return render(request, 'main/about.html')

def index(request):
    """Функция для главной страницы"""
    return render(request, 'main/index.html')

