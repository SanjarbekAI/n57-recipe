from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm


def test_form(request):
    if request.method == "GET":
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'form_app.html', context)
    elif request.method == "POST":
        form = UserForm(data=request.POST, files=request.FILES)
        form.save()
        return HttpResponse("Data came to here")
