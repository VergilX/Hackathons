from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("main", views.main, name="main"),
    path("dash", views.dash, name="dash"),
    path("products", views.products, name="products"),
    path("classroom", views.classroom, name="classroom"),
    path("profile", views.profile, name="profile"),

]