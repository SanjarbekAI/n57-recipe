from blogs.models import BlogCategoryModel

from django.db.models import Q

def run():
    # cat2 = BlogCategoryModel.objects.create(title='Blog category 2')
    # cat2 = BlogCategoryModel(title='Blog category 2')
    # cat2.save()

    # BlogCategoryModel.objects.filter(id=1).update(title='nimadir')
    # cat = BlogCategoryModel.objects.filter(id=1).update(title='nimadir')
    # cat.title = 'Yangi title'
    # cat.save()

    # cat1 = BlogCategoryModel.objects.get(id=2)
    # cat2 = BlogCategoryModel.objects.filter(id=2)
    # print(
    #     cat1, cat2
    # )

    # "select * from blog_category"
    # cats = BlogCategoryModel.objects.all()
    # print(cats)

    # "select title from blog_category"
    # cats = BlogCategoryModel.objects.values('title')
    # print(cats)

    "select * from blog_Category id > 2"
    """
    __gt > 
    __gte >=
    __lt <
    __lte <=
    __isnull
    
    
    relationships, select_related, fetch_related | JOIN
    aggrogate, annotate | avg, sum, max, min, len ...
    

    select * from bc where id=>1 and id<=100
    """

