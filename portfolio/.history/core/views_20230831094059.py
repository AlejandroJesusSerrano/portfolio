from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("<h1>Mi Pirtfolio</h1><h3>Página Principal</h3>")