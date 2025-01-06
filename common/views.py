from django.shortcuts import render





def recipies_page_view(request):
    return render(request, 'recipies/recipe_with_sidebar.html')


def blog_page_view(request):
    return render(request, 'blogs/blogs_list.html')


def category_page_view(request):
    return render(request, 'recipies/category.html')


def submit_page_view(request):
    return render(request, 'recipies/submit_recipe.html')


def login_page_view(request):
    return render(request, 'auth/login.html')
