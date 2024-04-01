from django.contrib.auth.models import AbstractUser
from django.db import models


class Shoppers(AbstractUser):
    city = models.CharField(max_length=60, default="")
    phone_number = models.CharField(max_length=10, default="")
    location = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.username
    pass
