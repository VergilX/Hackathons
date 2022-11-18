from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("website:home"))
    return render(request, 'index.html')

def home(request):
    if not request.user.is_authenticated:
        return render(request, "website/index.html", {
            "message": "Please log in first",
        })

    return render(request, "website/home.html", {
        'message', "Logged in successfully!"
    })