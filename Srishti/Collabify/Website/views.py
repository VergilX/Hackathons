from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import *

# Create your views here.
def home(request):
    """ For displaying home page. Contains html for login/register too """

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "Website/home.html")

def userpage(request):
    """ Function for user page display """
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Website:home"))
    user = request.user
    education = Education.objects.filter(user=user)
    work = WorkExperience.objects.filter(user=user)
    return render(request, "Website/user.html", {
        'items': [
            [r"", "CALENDAR"],
            [r"", "SETTINGS"],
            [r"", "PEOPLE"],
            ["{% url 'Website:project' %}", "PROJECTS"],
            [r"", "WORKPLACES"]
            ], # add links here after creating urls
        'user': user,
        "languages": [i.name for i in user.lang.all()],
        "clubs": [i.name for i in user.clubs.all()],
        "skills": [i.name for i in user.skills.all()],
        "summary": user.summary,
        "details": [[i.job, i.company, i.returnperiod(), i.description] for i in list(work)],
        "educationdetails": [[i.qualification, i.institution, i.returnperiod(), i.description] for i in list(education)],
        "reference": list(user.references.all()),
    })

def edit(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, "Website/home.html")
    if request.method == "POST":
        # do all error handling in js if possible
        # retrieving data
        data = request.POST

        # assigning them
        user.name = data["name"]
        user.email  = data["email"]
        user.address = data["address"]
        user.phone = data["phone"]
        user.summary = data["summary"]

        user.lang.set([Language.objects.get(name=i) for i in data.getlist("languages")])
        user.clubs.set([Club.objects.get(name=i) for i in data.getlist("clubs")])
        user.skills.set([Skill.objects.get(name=i) for i in data.getlist("skills")])

        if not data['job'] in [None, ""]:
            WorkExperience(user=user, 
                           job=data["job"],
                           company=data["company"],
                           description=data["desc"],
                           start_year=data["start"],
                           end_year=data["end"]).save()

        if not data['qualification'] in [None, ""]:
            Education(user=user,
                      qualification=data["qualification"],
                      description=data["description"],
                      start_year=data["estart"],
                      end_year=data["eend"]).save()

        user.references.set([Referee.objects.get(name=i) for i in data.getlist("references")])
        user.save()
        return HttpResponseRedirect(reverse("Website:user"))

    return render(request, "Website/edit.html", {
        "user": user,
        'items': [
            [r"", "CALENDAR"],
            [r"", "SETTINGS"],
            [r"", "PEOPLE"],
            [r"{% url 'Website:project' %}", "PROJECTS"],
            [r"", "WORKPLACES"]
            ],
        "languages": [i.name for i in Language.objects.all()],
        "clubs": [i.name for i in Club.objects.all()],
        "skills": [i.name for i in Skill.objects.all()],
        "referees": [i.name for i in Referee.objects.all()],
        "used": {"referees": [i for i in user.references.all()],},
    })

def project(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, "Website/home.html")
    
    return render(request, "Website/projects.html", {

    })