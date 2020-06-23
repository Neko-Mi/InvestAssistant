# users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(help_text="", label='Имя пользователя')
    email = forms.EmailField(help_text='', label="Электронная почта")
    password1 = forms.CharField(help_text='', label="Пароль")
    password2 = forms.CharField(help_text='', label="Повторите пароль")

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')