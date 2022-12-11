from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import CommandCreateForm, CreateNewBotForm
from .models import Bot

def func(request):
    return HttpResponse('123')

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


class BotAddCommand(View):
    """Class for create task"""
    template_name = 'constructor/bot-add-command.html'
    context_object_name = 'bots'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bots'] = self.objects.all()
        return context


    def get(self, request):
        """Func which answer the GET method
        return template with task form
        """

        return render(request,
                      self.template_name,
                      context={
                          "form": CommandCreateForm,
                          "bots": Bot.objects.all()
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
            """
            место для вызова функции которая перезаписывает код бота
            
            """
            return redirect('bots')
        else:
            context = {'form': form,
                       'errors': form.errors}
            return render(request, self.template_name, context)

