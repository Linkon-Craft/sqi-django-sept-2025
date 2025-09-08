from django.urls import path
from . import views

urlpatterns = [
    path('case/', views.case_studies, name = 'case_studies'),
]