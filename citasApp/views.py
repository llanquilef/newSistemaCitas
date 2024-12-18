from django.shortcuts import render, redirect
from .models import Cita, Servicio, Estilista, Cliente
from .forms import FormularioReservaHora, FormularioUsuarioRegistro
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User


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


@api_view(['POST'])
@permission_classes([AllowAny]) 
def Registro(request):

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data)
        user.save()
        
    print(request.data)

    return Response({}) 