from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


from .forms import CommandCreateForm, CreateNewBotForm
from .models import Bot, Command

from .bots.CreateBot import CreateBot





# Путь к папке bots. Для написания скрипта бота
import os
import sys
sys.path.append(os.path.join(os.getcwd()))


class BotList(View):

    template_name = 'constructor/bots-list.html'
    login_url = reverse_lazy('/authentication/')


    def get(self, request):
        """Func which answer the GET method
        return template with task form
        """

        return render(request,
                      self.template_name,
                      context={
                          "bots": Bot.objects.all(),
                          "commands": Command.objects.all()
                      }
                      )


class CreateNewBot(View):
    template_name = 'constructor/create-new-bot.html'

    def get(self, request):
        context = {
            'form': CreateNewBotForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateNewBotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bots')
        else:
            context = {
                'form': form,
                'errors': form.errors
            }
            return render(request, self.template_name)


class BotEdit(DetailView):
    template_name = 'constructor/bot.html'


    def get(self, request, pk):
        """Func which answer the GET method
        return template with task form
        """

        return render(request,
                      self.template_name,
                      context={
                          "commands": Command.objects.all().filter(bot_name=pk)
                      }
                      )


class CommandDeleteView(DeleteView):
    model = Command
    context_object_name = 'command'

    def get_success_url(self):
        agent_id = self.object.bot_name
        return reverse_lazy('bot-edit-page', kwargs={'pk': agent_id})



class BotAddCommand(View):
    """Class for create task"""
    template_name = 'constructor/bot-add-command.html'
    context_object_name = 'bots'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bots'] = self.objects.all().filter(user=self.request.user)
        return context


    def get(self, request):
        """Func which answer the GET method
        return template with task form
        """

        return render(request,
                      self.template_name,
                      context={
                          "form": CommandCreateForm,
                          "bots": Bot.objects.all(),
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
            commit.save()

            commands = Command.objects.all().filter(bot_name=self.request.POST.get('bot_name'))

            list_of_commands = []
            ######################
            # Place for script   #

            for command in commands:
                a = {'token': self.request.POST.get('bot_token'), 'name_bot': self.request.POST.get('bot_name'), 'target_message': command.message, 'answer': command.answer}
                list_of_commands.append(a)

            if list_of_commands:
                bot = CreateBot(path_out_file="TESTmain.py", requests_for_bot=list_of_commands)
            else: print('list is empty\n'*10)

            ######################

            return redirect('bots')
        else:
            context = {'form': form,
                       'errors': form.errors}
            return render(request, self.template_name, context)

