from django.urls import path
from . import views 

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('hobbies/', views.hobbies, name = 'hobbies'),
    path('goals/', views.goals, name = 'goals'),
]