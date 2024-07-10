from django.urls import reverse

from blog_stack.accounts.tests.factories import UserFactory


class TestIndex:
    def test_unauthenticated(self, client):
        """An unauthenticated user gets a valid response."""
        response = client.get(reverse("index"))
        assert response.status_code == 200

    def test_authenticated(self, client):
        """An authenticated user gets a valid response."""
        client.force_login(UserFactory())
        response = client.get(reverse("index"))
        assert response.status_code == 200


class TestTerms:
    def test_terms(self, client):
        """Test, The terms of service page of the application."""
        response = client.get(reverse("terms"))
        assert response.status_code == 200


class TestPrivacy:
    def test_privacy(self, client):
        """Test, The privacy of service page of the application."""
        response = client.get(reverse("privacy"))
        assert response.status_code == 200
