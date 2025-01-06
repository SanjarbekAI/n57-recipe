from blogs.models import BlogCategoryModel, BlogTagModel, BlogModel


def run():
    # tag = BlogTagModel.objects.create(title='tag')
    # cat = BlogCategoryModel.objects.get(id=1)
    #
    # blog = BlogModel(
    #     image1='',
    #     image2='',
    #     tags=tag,
    #     categories=cat,
    # )

    """
    ProductsModel.objects.filter(category__id=1)

    product = ProductsModels.objects.get(id=1)
    product.price = product.price * 1.1
    product.save()

    # ProductsModels.objects.aggrgate(Count('category')).values('id', 'categories__count')


    aggregate and annotate in django
    how to use OR in django | Q

    """
