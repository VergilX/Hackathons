from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Importing custom user
from .models import User

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("website:index"))

    # if data is sent to this URL
    if request.method == "POST":
        data = request.POST

        username = data["username"]
        if username not in [i.username for i in User.objects.all()]:
            user = User.objects.create_user(
                username=username,
                password=data.get("password"),
                email=data.get("email"),
                phone=data.get("phone")
            )

            # Setting if shop owner
            if (data.get("owner") == "yes"):
                user.is_owner = True

            user.name = data["name"]
            user.phone = data["phone"]

            user.save()
            login(request, user)

            return HttpResponseRedirect(reverse("website:index"))

        # if not authenticated
        else:
            return render(request, "website/index.html", {
                "message": "Username is already taken",
            })

    return render(request, "website/index.html")

def login_user(request):
    if request.user.is_authenticated:
        return render(request, 'website/index.html', {
            "message": "Already logged in"
        })

    if request.method == "POST":
        data = request.POST

        # authenticated user
        user = authenticate(request, username=data["username"], password=data["password"])


        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse("website:home"))

        return render(request, "website/index.html", {
            "message": "Invalid login credentials"
        })

    return render(request, "website/index.html")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, "website/index.html", {
            "message": "Logged out successfully"
        })

    return render(request, "website/index.html")