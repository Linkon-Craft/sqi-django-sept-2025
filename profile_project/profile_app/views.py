from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, "profile_apps/index.html")

def hobbies(request):
    return render(request, "profile_apps/hobbie.html")

def goals(request):
    return render(request, "profile_apps/goals.html")