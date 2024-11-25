from django import forms
from .models import Cita, Usuario

# Formulario Usuario
class usuarioFormulario(forms.ModelForm):
    model = Usuario
    fields = ['nombre','email','contraseña']

# Formulario Reserva Hora
class reservaHora(forms.ModelForm):
    model = Cita, Usuario
    fields = ['estilista', 'servicio', 'fecha', 'hora']