from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('confirm/email/<int:uid>/<str:token>/', views.confirm_email_view, name='confirm_email'),
]
