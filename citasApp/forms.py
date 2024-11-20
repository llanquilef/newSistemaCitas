from django import forms
from .models import Cita

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    email = forms.CharField()
    contraseña = forms.CharField()

class ReservaHora(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=320)
    fecha = forms.DateField()
    hora = forms.TimeField()
