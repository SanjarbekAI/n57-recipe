from django.urls import path

from pages.views import contact_page_view, about_page_view, home_page_view

app_name = 'pages'

urlpatterns = [
    path('about/', about_page_view, name='about'),
    path('contact/', contact_page_view, name='contact'),
    path('', home_page_view, name='home'),
]
