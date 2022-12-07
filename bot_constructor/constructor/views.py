from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):
    return HttpResponse('Main')

def createnewbot(request):
    return HttpResponse('Create new bot')

def BotAddCommand(request):
    return render(request, 'constructor/bot-add-command.html')

# class BotAddCommand(LoginRequiredMixin, View):
#     """Class for create task"""
#     template_name = 'constructor/bot-add-command.html'
#
#