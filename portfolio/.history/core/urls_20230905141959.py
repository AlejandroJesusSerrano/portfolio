from django.urls import path
from core import views

path('', views.home, name='home'),
path('about-me/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('portfolio/', views.portfolio, name='portfolio'),
path('curriculum/', views.curriculum, name='curriculum'),