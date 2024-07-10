from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog_stack.accounts"

    # def ready(self):
    #     try:
    #         import blog_stack.accounts.signals  # noqa: F401
    #     except ImportError:
    #         pass
