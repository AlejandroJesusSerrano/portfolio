from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("<h1>Mi Portfolio</h1><h3>Página Principal</h3>")

def about(request):
  return HttpResponse("<h1>Mi Porfolio Personal</h1><h3>Acerca de...</h3><p>Mi nombre es Alejandro Jesús Serrano y soy programador")