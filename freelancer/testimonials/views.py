from django.shortcuts import render

# Create your views here.

def testimonials(request):
    context = {
        "testimonials": {
            "Dan": "Good service, I really enjoyed shopping here!",
            "Paul": "Bad service, delivery was late.",
            "Mary": "Excellent customer support and fast delivery.",
            "James": "Affordable prices, will shop again.",
            "Ada": "Website is easy to use and checkout was smooth."
        }
    }
    return render(request, "testimonials.html", context)