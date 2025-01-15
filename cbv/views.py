from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views import View
from django.views.generic import FormView

from cbv.forms import LoginForm, MyForm


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'

    def form_valid(self, form):
        print("User logged in:", form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '/')


class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)  # Log out the user on GET
        return redirect('pages:contact')


class MyFormView(FormView):
    form_class = MyForm
    template_name = 'my_form.html'  # The template where the form will be rendered
    success_url = '/success/'  # Redirect URL after a successful form submission

    def form_valid(self, form):
        # This method is called when the form is valid
        # You can access form.cleaned_data here
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        return super().form_valid(form)

