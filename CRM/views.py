from django.shortcuts import render
from users.models import User
from django.views import View
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["User"] = User
        context["type_device"] = self.request.type_device
        return context


class TestView(TemplateView):
    template_name = "pc/test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["User"] = User
        context["type_device"] = self.request.type_device
        return context
