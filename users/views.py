import threading

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.shortcuts import render, redirect

from users.forms import RegisterForm, LoginForm
from users.models import CustomUserModel
from users.utils import send_email_confirmation


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(raw_password=request.POST['password1'])
            user.save()

            # sending email
            email_thread = threading.Thread(target=send_email_confirmation, args=(request, user,))
            email_thread.start()

            return render(request, 'auth/check_email.html')
    else:
        return render(request, 'auth/register.html')


def confirm_email_view(request, uid, token):
    try:
        user = CustomUserModel.objects.get(id=uid)
    except CustomUserModel.DoesNotExist:
        messages.error(request, "User not found")
        return redirect('users:register')

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'auth/email_confirmed.html')
    else:
        messages.error(request, "Token is invalid")
        return redirect('users:register')


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_username = request.POST['email_or_username']
            password = request.POST['password']

            try:
                user = CustomUserModel.objects.get(
                    Q(email=email_or_username) | Q(username=email_or_username)
                )
            except CustomUserModel.DoesNotExist:
                messages.error(request, "User not found")
                return redirect('users:login')

            authenticated_user = authenticate(username=user.username, password=password)
            if authenticated_user is not None:
                login(request, user)
                return redirect('pages:home')
            else:
                messages.error(request, "Username or password is invalid")
                return redirect('users:login')
        else:
            messages.error(request, "Username or password is invalid")
            return redirect('users:login')
    else:
        return render(request, 'auth/login.html')
