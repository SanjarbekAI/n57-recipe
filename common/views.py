from django.shortcuts import render


def home_page_view(request):
    return render(request, 'index.html')


def about_page_view(request):
    return render(request, 'pages/about.html')


def recipies_page_view(request):
    return render(request, 'recipies/recipe_with_sidebar.html')


def contact_page_view(request):
    return render(request, 'pages/contact.html')


def blog_page_view(request):
    return render(request, 'blogs/blogs_list.html')


def category_page_view(request):
    return render(request, 'recipies/category.html')


def submit_page_view(request):
    return render(request, 'recipies/submit_recipe.html')


def login_page_view(request):
    return render(request, 'auth/login.html')