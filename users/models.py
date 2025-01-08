from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserModel(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
