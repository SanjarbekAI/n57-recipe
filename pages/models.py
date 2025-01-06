from django.db import models

from common.models import BaseModel


class ContactModel(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
