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
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            context = {
                'errors': 'Login error,try again...'
            }
            return render(request, template_name, context)

    elif request.method == "POST" and 'register' in request.POST:
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            username = form.cleaned_data.get('username')
            password = make_password(form.cleaned_data.get('password'))
            email = form.cleaned_data.get('email')
            print('username', username)
            print('email', email)
            print('password', password)
            user = authenticate(request, username=username, password=password, email=email)

            if user is not None:
                login(request, user)
                return redirect('authentication')

        else:
            print('else')
            return render(request,
                          template_name,
                          context={
                              'form': form,
                              'errors': form.errors
                          }
                          )


def profile(request, pk):
    user_pk = CustomUser.objects.filter(username=pk)

    return render(request, 'profile.html', context={'user_pk': user_pk[0]})
