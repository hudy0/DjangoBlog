from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def account_list(request: HttpRequest) -> HttpResponse:
    template_name = "accounts/account_list.html"
    return render(request, template_name)
