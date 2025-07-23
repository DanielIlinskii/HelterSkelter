"""
URL configuration for CRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from booking.models import Booking
from .views import HomeView, TestView, BookingView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("", HomeView.as_view(), name="home"),
    path("booking/", BookingView.as_view(), name="booking"),
    path("test/", TestView.as_view(), name="base"),
]


# path("index/", index, name="index"),
# path("test/", type_device, name="type_device"),
# path("api/", include("api.urls")),
