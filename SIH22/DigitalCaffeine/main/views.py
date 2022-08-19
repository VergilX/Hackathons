from django.shortcuts import render
from main.models import Device
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def main(request):
    return render(request, "main/data.html")

def stats(request):
    return render(request, "main/stats.html")

def newpair(request, code=None):
    """ For pairing new device for new user """
    # check validity of "code" as positional argument
    device = Device.objects.get(code=code)
    if device is None:
        return render(request, "users/home.html", {
            "message": "This device is already paired to a user"
        })
    
    if request.method == "POST":
        print(code)
        return render(request, "users/home.html")

def dash(request):
    """ Function for displaying dash board """

    if request.user.is_authenticated:
        return render(request, "dash/index.html")
    return HttpResponseRedirect(reverse("users:home"))