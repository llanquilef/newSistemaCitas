from django.shortcuts import render, redirect
from .models import Cita, Servicio, Estilista, Cliente
from .forms import FormularioReservaHora, FormularioUsuarioRegistro

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
# Reserva Hora
def reservaHora(request):
    if request.method == "POST":
        form = FormularioReservaHora(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data.get('telefono', '')

            # Verifica si el cliente ya existe o crea uno nuevo
            cliente, created = Cliente.objects.get_or_create(
                email=email,
                defaults={
                    'nombre': nombre,
                    'telefono': telefono,
                    'contraseña': 'default_password',
                    'rol': 'cliente',
                }
            )
            # Asocia la cita al cliente
            cita = form.save(commit=False)  
            cita.cliente = cliente  
            cita.estado = 'Reservada' 
            cita.save()  
            return redirect('index')
    else:
        form = FormularioReservaHora()

    return render(request, 'reservaHora.html', {'form': form})

def usuarioRegistro(request):
    if request.method == "POST":
        formulario_registro = FormularioUsuarioRegistro(request.POST)
        if formulario_registro.is_valid():
            formulario_registro.save()
            return redirect('index')
    else:
        formulario_registro = FormularioUsuarioRegistro()
    
    return render(request, 'registroUsuario.html', {'formulario_registro':formulario_registro})
