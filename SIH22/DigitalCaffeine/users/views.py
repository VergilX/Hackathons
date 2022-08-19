from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# importing custom user
from .models import MyUserManager, User

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return render(request, "main/index.html", {
            "message": "Please sign in",
        })
    return render(request, "dash/index.html")

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:home"))

    # if data is sent to this URL
    if request.method == "POST":
        data = request.POST # received data
        
        username = data["username"]
        if username not in [i.username for i in User.objects.all()]:
            user = User.objects.create_user(
                username=username,
                password=data.get("password"),
                email=data.get("email"),
                phone=data.get("phone"),
                code = "",
            )

            user.name = data["name"]
            user.phone = data["phone"]
            
            user.save()
            login(request, user)

            return HttpResponseRedirect(reverse("users:home"))

        else:
            return render(request, "users/register.html", {
                "message": "Username is already taken",
                # add things for already showing details typed
            })

    return render(request, "users/register.html")

def login_user(request):
    if request.user.is_authenticated:
        return render(request, "dash/index.html")
    
    if request.method == "POST":
        data = request.POST
        
        # authenticating user
        user = authenticate(request, username=data["username"], password=data["password"])

        if user is not None:
            login(request, user)
            return render(request, "dash/index.html")

        return render(request, "main/index.html", {
            "message": "Invalid login credentials"
        })

    return render(request, "users/login.html")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, "main/index.html", {
            "message": "Logged out successfully"
        })
    return render(request, "main/index.html")
    