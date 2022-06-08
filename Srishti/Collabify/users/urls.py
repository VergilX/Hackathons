from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.login_home, name="login"),
    path("logout", views.logout_home, name="logout"),
    path("register", views.register, name="register"),
]