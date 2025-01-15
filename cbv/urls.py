from django.contrib.auth.views import LogoutView
from django.urls import path

from cbv.views import CustomLoginView, CustomLogoutView

app_name = 'cbv'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]
