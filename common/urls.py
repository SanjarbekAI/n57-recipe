from django.urls import path

from common.views import *

app_name = 'pages'

urlpatterns = [
    path('about/', about_page_view, name='about'),
    path('contact/', contact_page_view, name='contact'),
    path('submit/', submit_page_view, name='submit'),
    path('recipies/', recipies_page_view, name='recipies'),
    path('login/', login_page_view, name='login'),
    path('category/', category_page_view, name='category'),
    # path('shop/', about_page_view, name='about'),
    path('', home_page_view, name='home'),
]
