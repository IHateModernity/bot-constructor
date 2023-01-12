from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateNewBotForm

from .forms import CommandCreateForm, CreateNewBotForm
from .models import Bot, Command

from .bots.CreateBot import CreateBot

import hashlib
import os
import sys
sys.path.append(os.path.join('../../')) # Путь к папке bots. Для написания скрипта бота


class BotList(LoginRequiredMixin, View):
    model = Bot
    template_name = 'constructor/bots-list.html'
    context_object_name = 'bots'


    def get(self, request):
        """Func which answer the GET method
        return template with task form
        """

        return render(request,
                      self.template_name,
                      context={
                          "bots": Bot.objects.all().filter(user=self.request.user),
                          "commands": Command.objects.all()
                      }
                      )

    def post(self, request):
        a = request.POST
        bot_name, token = [i for i in a][1].split()

        ######################
        # Creating script   #
        commands = Command.objects.all().filter(bot_name=bot_name)

        list_of_commands = []

        for command in commands:
            a = {'token': token, 'name_bot': bot_name,
                 'target_message': command.message, 'answer': command.answer}
            list_of_commands.append(a)

        path = hashlib.md5(token.encode())
        path = "media/scripts/" + bot_name + '_' + path.hexdigest() + ".py"
        print(path)
        if list_of_commands:
            script = CreateBot(path_out_file=path, requests_for_bot=list_of_commands)
            bot = Bot.objects.get(bot_username=bot_name)
            bot.has_script = True
            bot.script_path = path[6:]
            bot.save()
            return redirect('bots')
        else:
            print('list is empty\n' * 10)
        ######################


        return redirect('bots')


class CreateNewBot(LoginRequiredMixin, CreateView):
    template_name = 'constructor/create-new-bot.html'

    def get(self, request):
        """Func which answer the GET method
        return template with task form
        """

        return render(request,
                      self.template_name,
                      context={
                          "form": CreateNewBotForm
                      }
                      )

    def post(self, request):
        form = CreateNewBotForm(request.POST)
        if form.is_valid():
            commit = form.save(commit=False)
            commit.user = request.user
            form.save()

            return redirect('bots')
        else:
            context = {
                'form': form,
                'errors': form.errors
            }
            return render(request, self.template_name, context)



#### FOR COMMANDS ####
class BotAddCommand(LoginRequiredMixin, View):
    """Class for create task"""
    template_name = 'constructor/bot-add-command.html'

    def get(self, request):
        """Func which answer the GET method
        return template with task form
        """

        return render(request,
                      'constructor/bot-add-command.html',
                      context={
                          "form": CommandCreateForm,
                          "bots": Bot.objects.all().filter(user=self.request.user),
                      }
                      )

    def post(self, request):
        """Func which answer the POST method

        if form valid: get and save the form
        else: return form and errors
        """
        form = CommandCreateForm(request.POST)
        if form.is_valid():
            commit = form.save(commit=False)
            commit.user = request.user
            bot = Bot.objects.get(bot_username=commit.bot_name)
            commit.bot_token = bot.bot_token
            commit.save()

            return redirect('bots')

        else:
            print('error\n'*10)
            context = {'form': form,
                       'errors': form.errors}
            return render(request, self.template_name, context)


class BotCommandList(LoginRequiredMixin, DetailView):
    template_name = 'constructor/bot_edit.html'


    def get(self, request, pk):
        """Func which answer the GET method
        return template with task form
        """

        return render(request,
                      self.template_name,
                      context={
                          "commands": Command.objects.all().filter(bot_name=pk),
                          'bot': pk
                      }
                      )


class CommandDeleteView(LoginRequiredMixin, DeleteView):
    model = Command
    context_object_name = 'command'

    def get_success_url(self):
        command_id = self.object.bot_name
        return reverse_lazy('bot-edit-page', kwargs={'pk': command_id})


class CommandEditView(LoginRequiredMixin, UpdateView):
    model = Command
    fields = ['type', 'message', 'answer', ]
