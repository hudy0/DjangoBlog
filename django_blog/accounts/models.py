# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_pic = models.ImageField(default="default.jpg", upload_to="profile_pics", blank=True, null=True)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
