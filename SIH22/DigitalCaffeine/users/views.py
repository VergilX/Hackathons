from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "users/home.html")

def login(request):
    pass

def logout(request):
    pass

def register(request):
    pass