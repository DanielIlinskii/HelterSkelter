from django.urls import path
from .views import UserListCreateView, test

urlpatterns = [
    path("api/users/", UserListCreateView.as_view(), name="user-list-create"),
    path("test/", test, name="test"),
]
