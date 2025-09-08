from django.shortcuts import render

# Create your views here.

def pricing(request):
    context = {
        "services": {
            "Logo Design": "$10,000",
            "Backend Development": "$6,500",
            "Frontend Development": "$5,000",
            "UI/UX Design": "$4,000",
            "SEO Optimization": "$3,500"
        }
    }
    return render(request, "pricing.html", context)