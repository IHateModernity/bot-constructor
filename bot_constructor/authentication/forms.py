from django import forms
from django.contrib.auth import get_user_model
from django.forms import models
from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    """Form registration new user"""
    # переменная = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) НЕ ТРОГАЙТЕ ЭТУ ХНЮ

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2',)
