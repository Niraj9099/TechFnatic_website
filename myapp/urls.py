from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('card/<int:pk>', views.card, name='card'),
    path('contact/', views.contactForm, name='contact'),
    path('policy/', views.privatePolicy, name='policy'),
    path('terms_condition/', views.terms_condition, name='terms_condition'),
]