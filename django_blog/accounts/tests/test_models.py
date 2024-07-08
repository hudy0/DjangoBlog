import pytest

from django_blog.accounts.tests.factories import AccountFactory, UserFactory


# @pytest.mark.django_db
class TestUser:
    def test_factory(self):
        """The factory produces a valid instance."""
        user = UserFactory()

        assert user is not None


@pytest.mark.django_db
class TestAccount:
    """The factory produces a valid instance."""

    def test_factory(self):
        account = AccountFactory()

        assert account is not None
        assert account.user is not None
