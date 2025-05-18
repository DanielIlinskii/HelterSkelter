from django.http import HttpResponse, HttpRequest
from django_user_agents.utils import get_user_agent
from django.shortcuts import render
from django.contrib.auth.models import User


def type_device(request) -> str:
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return "mobile"
    elif user_agent.is_pc:
        return "pc"
    elif user_agent.is_tablet:
        return "tablet"


def index(request):
    return render(request, "admin_panel/" + type_device(request) + "/index.html")


def main(request):
    context = {
        "User": User
    }
    return render(request, "site/base.html", context)
