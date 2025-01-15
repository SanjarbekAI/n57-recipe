from django.urls import path

from blogs.views import blog_list_view, blog_detail_view, blog_comment_view

app_name = 'blogs'

urlpatterns = [
    path('<int:pk>/', blog_detail_view, name='detail'),
    path('<int:pk>/comment/', blog_comment_view, name='comment'),
    path('', blog_list_view, name='list'),
]
