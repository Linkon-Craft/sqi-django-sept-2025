from django.shortcuts import render, HttpResponse

# Create your views here.


def incoming(request):
    return HttpResponse("incoming: 'Welcome to the Blog Home'")


def post(request):
    return HttpResponse("post: 'This is blog post #1'")

def about(request):
    return HttpResponse("about: 'About the Blog'")