from django.urls import path
from . import views

app_name = "Website"

urlpatterns = [
    path("", views.home, name="home"),
    path("profile", views.userpage, name="user"),
]