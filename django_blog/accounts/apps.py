from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_blog.accounts"

    def ready(self):
        try:
            import django_blog.accounts.signals  # noqa: F401
        except ImportError:
            pass
