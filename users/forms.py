from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class LoginForm(forms.Form):
    email_or_username = forms.CharField(max_length=128, label="Email or Username")
    password = forms.CharField(max_length=128)
