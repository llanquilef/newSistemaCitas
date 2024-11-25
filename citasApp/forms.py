from django import forms
from .models import Cita


# Formulario Reserva Hora
class FormularioReservaHora(forms.ModelForm):
    model = Cita
    fields = ['estilista', 'servicio', 'fecha', 'hora']