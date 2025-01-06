from django import forms

from app_form.models import UserFormModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserFormModel
        # fields = ['full_name', 'age', 'image']
        # exclude = ['created_at']
        fields = '__all__'
