import factory
from django.db.models.signals import post_save


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.User"

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")


@factory.django.mute_signals(post_save)
class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.Account"

    user = factory.SubFactory("django_blog.accounts.tests.factories.UserFactory")
