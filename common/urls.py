from django.urls import path

from common.views import *

app_name = 'common'

urlpatterns = [
    path('submit/', submit_page_view, name='submit'),
    path('recipies/', recipies_page_view, name='recipies'),
    path('login/', login_page_view, name='login'),
    path('category/', category_page_view, name='category'),
    path('blog/', blog_page_view, name='blog'),
]
