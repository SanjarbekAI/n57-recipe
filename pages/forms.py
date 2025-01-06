from django import forms

from pages.models import ContactModel


class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['phone_number']


class ContactAboutPageForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['subject']
