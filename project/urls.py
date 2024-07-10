"""
URL configuration for project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from blog_stack.core.views import index, privacy, terms

urlpatterns = [
    # django-allauth main url
    path("accounts/", include("allauth.urls")),
    # django admin url
    path(settings.DJANGO_ADMIN_URL, admin.site.urls),
    # core app urls path
    path("", view=index, name="index"),
    path("terms/", view=terms, name="terms"),
    path("privacy/", view=privacy, name="privacy"),
]
