from django.contrib.auth import get_user_model
from django.db import models

from common.models import BaseModel

User = get_user_model()


class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog category"
        verbose_name_plural = "Blog categories"


class BlogTagModel(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog tag"
        verbose_name_plural = "Blog tags"


class BlogModel(BaseModel):
    title = models.CharField(max_length=128)
    image1 = models.ImageField(upload_to='blogs')
    image2 = models.ImageField(upload_to='blogs')
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()

    categories = models.ManyToManyField(BlogCategoryModel, related_name='blogs')
    tags = models.ManyToManyField(BlogTagModel, related_name='blogs')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class BlogCommentModel(BaseModel):
    comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Blog comment"
        verbose_name_plural = "Blog comments"


class BlogLikeModel(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_likes')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user.get_full_name()} liked to {self.blog.title}'

    class Meta:
        verbose_name = "Blog like"
        verbose_name_plural = "Blog likes"
