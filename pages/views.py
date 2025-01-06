from django.contrib import messages
from django.shortcuts import render

from .forms import ContactPageForm


def about_page_view(request):
    return render(request, 'pages/about.html')


def contact_page_view(request):
    if request.method == "GET":
        return render(request, 'pages/contact.html')
    elif request.method == "POST":
        form = ContactPageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your contact information is sent to database")
        else:
            messages.success(request, form.errors)
        return render(request, 'pages/contact.html')


def home_page_view(request):
    return render(request, 'index.html')
