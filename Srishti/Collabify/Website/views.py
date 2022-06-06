from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    """ For displaying home page. Contains html for login/register too """

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "Website/home.html")

def register(request):
    if request.method == "POST":
        # collecting data
        data = request.POST
        username = data["username"]

        # All users
        users = User.objects.all()
        if username not in [i.username for i in users]:
            # rest of the data
            password = data["password"]
            # Confirm password == password will be checked using Js
            phone = data["phone"]
            email = data["email"]

            # create user, login and return login page
            # Need to create a new table for Person

def login_home(request):
    if request.method == "POST":
        # collecting data
        data = request.POST
        username = data["username"]
        password = data["password"]
        
        user = authenticate(request, username=username, password=password)
        
        # If credentials are correct
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("user"))
        return render(request, "Website/home.html", {
            "msg": "Incorrect credentials",
        })

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))
    # If the request made is not POST and not already logged in
    return render(request, "Website/home.html")

def logout_home(request):
    return render(request, "Website/home.html")

def userpage(request):
    """ Function for user page display """
    pass