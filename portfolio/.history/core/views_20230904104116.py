from django.shortcuts import render, HttpResponse

html_header = """
<h1>Mi Portfolio Personal</h1>
  <ul>
    <li> <a href="/">Inicio</a> </li>
    <li> <a href="/about-me/">Acerca de Mi</a> </li>
    <li> <a href="/portfolio/">Portfolio</a> </li>
    <li> <a href="/curriculum/">Curriculum</a> </li>
    <li> <a href="/contact/">Contáctame</a> </li>
  </ul>
"""
# Create your views here.
def home(request):
  return HttpResponse(html_header + "<h3>Página Principal</h3>")

def about(request):
  return HttpResponse(html_header + "<h3>Acerca de Mi</h3><p>Mi nombre es Alejandro Jesús Serrano y soy programador")

def portfolio(request):
  return HttpResponse(html_header + "<h3>Portfolio</h3><p>Estos son los proyectos que he desarrollado</p>")

def curriculum(request):
  return HttpResponse(html_header + "<h3>Curriculum</h3><p>Especializaciones...</p><p>Futuros Conocimientos</p><p>Aprendiendo Actualmente</p>")

def contact(request):
  return HttpResponse(html_header + "<h3>Contacto</h3><p>Por favor complete el formulario de contacto</p>")