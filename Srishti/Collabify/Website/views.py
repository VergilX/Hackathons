from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    """ For displaying home page. Contains html for login/register too """

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Website:login"))
    return render(request, "Website/home.html")

def userpage(request):
    """ Function for user page display """
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Website:home"))
    return render(request, "Website/user.html", {
        'items': [
            ["", "CALENDAR"],
            ["", "SETTINGS"],
            ["", "PEOPLE"],
            ["", "PROJECTS"],
            ["", "WORKPLACES"]
            ], # add links here after creating urls
    })