from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, "test.html")


# аутентификация
class LoginView(View):
    def get(self, request):
        return render(request, f"site/{request.type_device}/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect("/")
