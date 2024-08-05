# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Employees
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    class Meta:
        model = Employees
        fields = ('email', 'name', 'birthdate', 'date_of_joining', 'position', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = Employees
        fields = ('username', 'password')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        cleaned_data['email'] = username
        return cleaned_data


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['name', 'email', 'password', 'position', 'date_of_joining', 'birthdate', 'role']
