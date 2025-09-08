from django.shortcuts import render

# Create your views here.

def blog(request):
   context = {
        "posts": [
            {
                "title": "How Digital Payments Are Changing Small Businesses",
                "author": "Admin",
                "date": "September 1, 2025",
                "content": "Digital wallets and online payment solutions like PayOwner are helping small businesses expand beyond local markets."
            },
            {
                "title": "5 Tips for Managing Your Business Finances",
                "author": "Finance Team",
                "date": "August 25, 2025",
                "content": "From tracking expenses to automating payroll, learn how to simplify your business accounting process."
            }
        ]
    }
   return render(request, "blog.html", context)