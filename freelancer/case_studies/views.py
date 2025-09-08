from django.shortcuts import render

# Create your views here.

def case_studies(request):
    context = {
        "studies": [
            {
                "title": "PayOwner Helps Local Grocery Store Increase Sales by 40%",
                "summary": "By adopting PayOwner’s seamless checkout, Mama Tega’s Grocery reduced queues and saw a 40% sales boost within 3 months."
            },
            {
                "title": "How a Startup Streamlined Payroll with PayOwner",
                "summary": "A tech startup automated salary payments for 20 employees, saving hours of manual work every month."
            }
        ]
    }
    return render(request, "case_studies.html", context)
