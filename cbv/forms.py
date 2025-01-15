from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    email_or_username = forms.CharField(max_length=128, label="Email or Username")
    password = forms.CharField(
        max_length=128, widget=forms.PasswordInput, label="Password"
    )

    def clean(self):
        email_or_username = self.cleaned_data.get("email_or_username")
        password = self.cleaned_data.get("password")

        if not email_or_username or not password:
            raise forms.ValidationError("Both fields are required.")

        user = None

        # Try to authenticate by email first
        try:
            user_by_email = User.objects.get(email=email_or_username)
            user = authenticate(username=user_by_email.username, password=password)
        except User.DoesNotExist:
            # If no email match, fallback to authenticate by username
            user = authenticate(username=email_or_username, password=password)

        if user is None:

            raise forms.ValidationError("Invalid email/username or password.")

        if not user.is_active:
            raise forms.ValidationError("This account is inactive.", code="inactive")

        # Attach the authenticated user to the form
        self.user_cache = user
        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()