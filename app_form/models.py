from django.db import models


class UserFormModel(models.Model):
    full_name = models.CharField(max_length=128)
    age = models.PositiveSmallIntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.full_name
