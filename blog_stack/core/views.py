from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """The entry point of the application."""
    context = {}
    template_name = "core/unauthenticated.html"
    if request.user.is_authenticated:
        template_name = "core/index.html"
    return render(request, template_name, context)


def terms(request: HttpRequest) -> HttpResponse:
    """The terms of service page of the application."""
    context = {}
    return render(request, "core/terms.html", context)


def privacy(request: HttpRequest) -> HttpResponse:
    """The privacy of service page of the application."""
    context = {}
    return render(request, "core/privacy.html", context)
