from django.db import models

from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=320)
    contraseña = models.CharField(max_length=128)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}, {self.email}, {self.rol}'

    
class Administrador(Usuario):
    pass

class Estilista(Usuario):
    especialidades = models.CharField(max_length=1000)
    horario = models.JSONField()


class Cliente(Usuario):
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre}, {self.email}"

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    duracion = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.nombre}  (${self.precio})"

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estilista = models.ForeignKey(Estilista, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=[
        ('Reservada', 'Reservada'),
        ('Cancelada', 'Cancelada'),
        ('Completada', 'Completada'),
        ])
    def __str__(self):
        return f"Estado Reserva: {self.estado} - Fecha y Hora: {self.fecha}, {self.hora} - Estilista: {self.estilista} - Servicio: {self.servicio}"
    
class Horario(models.Model):
    dia_semana = models.CharField(max_length=20)
    horas_disponibles = models.JSONField()

    def __str__(self): 
        return self.dia_semana