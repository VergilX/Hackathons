from django.shortcuts import render
from users.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def register(request):
    if request.method == "POST":
        # collecting data
        data = request.POST
        username = data.get("username")

        # All users
        users = User.objects.all()
        if username not in [i.username for i in users]:
            # rest of the data
            password = data.get("password")
            # Confirm password == password will be checked using Js
            phone = data.get("phone")
            email = data.get("email")
            password = data.get("password")

            # create user, login and return login page
            user = User.objects.create_user(email=email,
                        username=username,
                        password=password)

            # adding phone
            user.phone = phone

            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("Website:user"))
        return render(request, "Website/home.html")
    return HttpResponseRedirect(reverse("Website:home"))

def login_home(request):
    if request.method == "POST":
        # collecting data
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        
        user = authenticate(request, username=username, password=password)
        # If credentials are correct
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("Website:user"))
        print("incorrect")
        return render(request, "Website/home.html", { # change this with js
            "msg": "Incorrect credentials",
        })

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Website:home"))
    # If the request made is not POST and not already logged in
    return render(request, "Website/home.html")

def logout_home(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, "Website/home.html")
    return render(request, "Website/home.html")