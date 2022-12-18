from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate
# Create your views here.
from django.views import View
from django.contrib.auth import views, login

from .models import CustomUser


def authenticate_(request):
    """Authentication func
    can login and register and same page"""
    template_name = 'registration/auth.html'

    if request.method == "GET":
        context = {
            'form': UserRegistrationForm
        }
        return render(request, template_name, context)

    if request.method == "POST" and 'login' in request.POST:

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)

        print('\n' * 10, username, password, '\n' * 10)


        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            context = {
                'errors': 'Login error,try again...'
            }
            return render(request, template_name, context)


    elif request.method == "POST" and 'register' in request.POST:
        form = UserRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()


            username = form.cleaned_data.get('username') # ?????????????
            password = form.cleaned_data.get('password1')

            user.set_password(password)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print('\n' * 10, user.password, user.username, '\n'*10)

            return redirect('home')


        else:

            return render(request,
                          template_name,
                          context={
                              'form': form,
                              'errors': form.errors
                          }
                          )


class ProfileView(View):
    """Profile view"""
    template_name = 'profile.html'

    def get(self, request, pk):
        user_pk = CustomUser.objects.get(username=pk)
        return render(request, self.template_name, context={'user_pk': user_pk})

    def post(self, request, pk):
        user_pk = CustomUser.objects.get(username=pk)

        telegram_id = request.POST['telegram_id']
        if telegram_id != '':
            if telegram_id[0] != '@':
                return render(request, self.template_name, context={
                    'user_pk': user_pk,
                    'info': 'Not valid telegram_id'}
                    )
            else:
                user_pk.telegram_id = telegram_id
        if request.FILES != {}:
            user_pk.avatar = request.FILES['file']

        user_pk.save()

        return render(request, self.template_name, context={
                    'user_pk': user_pk,
                    'info': 'Successfully updated'}
                    )
