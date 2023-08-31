from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("<h1>Mi Portfolio</h1><h3>Página Principal</h3>")

def about(request):
  return HttpResponse("<h1>Mi Porfolio Personal</h1><h3>Acerca de...</h3><p>Mi nombre es Alejandro Jesús Serrano y soy programador")

def contact(request):
  return HttpResponse("<h1>Mi Portfolio Personal</h1><h3>Contacto</h3><p>Por favor complete el formulario de contacto</p>")

def portfolio(request):
  return HttpResponse("<h1>Mi Portfolio Personal</h1><h3>Proyectos</h3><p>Estos son los proyectos que he desarrollado</p>")

def curriculum(request):
  return HttpResponse("<h1>Mi Portfolio Personal</h1><h3>Habilidades y Especialidades</h3><p>Especializaciones...</p><p>Futuros Conocimientos</p><p>Aprendiendo Actualmente</p>")