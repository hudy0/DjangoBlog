from django.db.models.signals import post_save
from django.dispatch import receiver

from django_blog.accounts.models import Account, User


@receiver(post_save, sender=User)
def created_account(sender, instance, created, **kwargs):
    """A new user gets an associated account."""
    if created:
        Account.objects.create(user=instance)
