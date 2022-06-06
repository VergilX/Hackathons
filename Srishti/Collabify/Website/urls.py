from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_home, name="login"),
    path("logout", views.logout_home, name="logout"),
    path("register", views.register, name="register"), 
    path("profile", views.userpage, name="user")
]