from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name = 'homepage'),
    path('profile/', views.profile, name = 'profile'),
    path('services/', views.services, name = 'services'),
    path('help/', views.help, name = 'help'),
]