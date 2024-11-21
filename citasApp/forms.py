from django import forms
from .models import Cita, Usuario

class usuarioFormulario(forms.Form):
    nombre = forms.CharField()
    email = forms.CharField()
    contraseña = forms.CharField()

class ReservaHora(forms.ModelForm):
    model = Cita, Usuario
    fields = ['estilista', 'servicio', 'fecha', 'hora']