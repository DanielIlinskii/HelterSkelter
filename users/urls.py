from django.urls import path
from .views import IndexView, LoginView

urlpatterns = [
    path("", IndexView.as_view(), name="test"),
    path("login/", LoginView.as_view(), name="user_login"),
    path("profile/", IndexView.as_view(), name="profile"),
]

# path("logout/", LoginView.as_view(), name="user_logout"),
