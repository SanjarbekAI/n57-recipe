from django import forms

from blogs.models import BlogCommentModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = BlogCommentModel
        fields = ['comment']
