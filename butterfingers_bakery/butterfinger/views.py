from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "butterfinger/home.html")

def about(request):
    return render(request, 'butterfinger/about.html')

def menu(request):
    return render(request, 'butterfinger/menu.html')

def contact(request):
    return render(request, 'butterfinger/contact.html')