from django.shortcuts import render, HttpResponse

# Create your views here.


def welcome(request):
    return HttpResponse("welcome: 'Welcome to the Shop Home'")

def cart(request):
    return HttpResponse("cart: 'Your Shopping cart is empty'")