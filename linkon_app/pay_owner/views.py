from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'myapp\home.html')

def profile(request):
    return render(request, 'myapp/profile.html')

def services(request):
    return render(request, 'myapp/services.html')

def help(request):
    return render(request, 'myapp/help-desk.html')