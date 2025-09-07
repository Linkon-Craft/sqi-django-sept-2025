from django.shortcuts import render, HttpResponse

# Create your views here.

# MVT - MODEL-VIEW-TEMPLATE
# MVC - MODEL-VIEW-CONTROLLER

def contact_us(request):
    return HttpResponse("Contact us: '08166243885'")

def email_us(request):
    return HttpResponse("Email us: 'oyewoleolamilekan208@gmail.com'")