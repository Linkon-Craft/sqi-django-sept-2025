from django.shortcuts import render

# Create your views here.

def services(request):
    context = {
        "services": [
            "Logo Design",
            "Backend Development",
            "Frontend Development",
            "UI/UX Design",
            "SEO Optimization"
        ]
    }
    return render(request, "services.html", context)