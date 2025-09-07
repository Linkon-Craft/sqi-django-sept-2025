from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.shopping_cart, name = 'shopping_cart')
]