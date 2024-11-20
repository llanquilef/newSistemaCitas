from django import forms
from .models import Cita

class CitaFormulario(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['cliente', 'estilista', 'servicio', 'fecha', 'hora', 'estado']                    

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    email = forms.CharField()
    contraseña = forms.CharField()