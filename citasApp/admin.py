from django.contrib import admin
from .models import Usuario, Cita, Servicio, Estilista, Cliente

admin.site.register(Usuario)
admin.site.register(Cita)
admin.site.register(Servicio)
admin.site.register(Estilista)
admin.site.register(Cliente)