from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import CommandCreateForm

def createnewbot(request):
    return HttpResponse('Create new bot')

def func(request):
    return HttpResponse('123')

class BotAddCommand(LoginRequiredMixin, View):
    """Class for create task"""
    template_name = 'constructor/bot-add-command.html'

    def get(self, request):
        """Func which answer the GET method
        return template with task form
        """

        return render(request,
                      self.template_name,
                      context={
                          "form": CommandCreateForm
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
            return redirect('tasks')
        else:
            context = {'form': form,
                       'errors': form.errors}
            return render(request, self.template_name, context)

