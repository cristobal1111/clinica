from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import pacienteForm
from .models import paciente

# Create your views here.

def index(request):
    return render(request, 'paginas/index.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def login(request):
    formulario = pacienteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('paciente')
    return render(request, 'paginas/login.html', {'formulario' : formulario})

def especialistas(request):
    return render(request, 'paginas/especialistas.html')

def saludmental(request):
    return render(request, 'paginas/saludmental.html')

def talleres(request):
    return render(request, 'paginas/talleres.html')

def cita(request):
    return render(request, 'paginas/cita.html')