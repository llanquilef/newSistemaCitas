from django.shortcuts import render, redirect
from .models import Cita, Servicio, Estilista
from .forms import reservaHora, usuarioFormulario

# Index
def Index(request):
    return render(request, 'index.html')

# Listado de Citas 
def listadoCita(request):
    citas = Cita.objects.all()
    return render(request, 'listadoCitas.html', {'citas': citas})

# Listado Servicios
def Servicios(request):
    servicio = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicio': servicio})

# Listado Estilistas
def ListadoEstilistas(request):
    estilistas = Estilista.objects.all()
    return render(request, 'estilistas.html', {'estilistas':estilistas})

# Registro Usuario
def usuarioRegistro(request):
    if request.method == "POST":
        formulario_registro = usuarioFormulario(request.POST)
        if formulario_registro.is_valid():
            formulario_registro.save()
            return redirect('listadoCitas')
        else:
            formulario_registro = usuarioFormulario(request.POST)
            return render(request, 'usuarioRegistro', {'formulario_registro':usuarioFormulario})

# Reserva Hora
def reservaHora(request):
    return render(request, 'reservaHora.html')