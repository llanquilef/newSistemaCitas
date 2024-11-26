from django import forms
from .models import Cita, Usuario


# Formulario Reserva Hora
class FormularioReservaHora(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label="Nombre del Cliente" , required=False)
    email = forms.EmailField(max_length=320, label="Correo Electrónico" , required=False)
    telefono = forms.CharField(max_length=15, required=False, label="Teléfono")

    class Meta:
        model = Cita
        fields = ['estilista', 'servicio', 'fecha', 'hora']

class FormularioUsuarioRegistro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contraseña', 'rol']