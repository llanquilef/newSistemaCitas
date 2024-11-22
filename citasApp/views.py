from django.shortcuts import render
from django.urls import reverse_lazy
from citasApp import forms
from .models import Cita, Estilista, Servicio
from django.views.generic import CreateView, UpdateView, DeleteView


# Index
def Index(request):
    return render(request, 'index.html')

# Listado de Citas 
def listadoCita(request):
    citas = Cita.objects.all()
    return render(request, 'listadoCitas.html', {'citas': citas})

# Crear Cita
class CrearCita(CreateView):
    model = Cita
    fields = ['cliente', 'estilista', 'servicio', 'fecha', 'hora', 'estado']
    template_name = 'citas/crearCitas.html'
    success_url = reverse_lazy('index')

# Eliminar Cita
class EliminarCita(DeleteView):
    model = Cita 
    template_name = 'citas/eliminarCita.html'
    success_url = reverse_lazy('listadoCitas')

#Actualizar Cita
class ActualizarCita(UpdateView):
    model = Cita
    fields = ['cliente', 'estilista', 'servicio', 'fecha', 'hora', 'estado']
    template_name = 'citas/actualizarCita.html'
    success_url = reverse_lazy('listadoCitas')

# Crear producto 
def crearEstilista(request):
    Estilista.objects.create(nombre="Jazmín Rosalba", especialidades = 'Corte de Pelo, Decoloración y Tintura')
    return render(request, 'estilistaCreado.html')


# Listado Servicios
def Servicios(request):
    servicio = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicio': servicio})

# Registro Usuario
def UsuarioRegistro(request):
    formulario = forms.usuarioFormulario()
    data = {
        'formulario': formulario
    }
    return render(request, 'usuarioFormulario.html', data)

# Reserva Hora
def ReservaHora(request):
    formulario_reserva = forms.usuarioFormulario()
    data = {
        ''
    } 
    return render(request, 'reservaHora.html')