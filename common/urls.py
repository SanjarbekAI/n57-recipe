from django.urls import path

from common.views import home_page_view, about_page_view

app_name = 'pages'

urlpatterns = [
    path('about/', about_page_view, name='about'),
    path('', home_page_view, name='home'),
]
