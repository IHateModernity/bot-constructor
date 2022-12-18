from django import forms
from django.contrib.auth import get_user_model
from django.forms import models
from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    """Form registration new user"""
    email = forms.EmailField()  # widget=forms.EmailInput(attrs={'class': 'form-control'})
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2',)

