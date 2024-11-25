from django.shortcuts import render, redirect
from .models import Cita, Servicio, Estilista
from .forms import FormularioReservaHora

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


# Reserva Hora
def reservaHora(request):
    if request.method == "POST":
        form = FormularioReservaHora(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = FormularioReservaHora()
            
            return render(request, 'reservaHora.html', {'form': form})
    