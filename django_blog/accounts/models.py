from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    pass


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def created_account(sender, instance, created, **kwargs):
    """A new user gets an associated account."""
    if created:
        Account.objects.create(user=instance)
