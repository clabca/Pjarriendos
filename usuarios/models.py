from django.contrib.auth.models import AbstractUser
from django.db import models

class PerfilUsuario(AbstractUser):
    USUARIO_CHOICES = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )
    tipo_usuario = models.CharField(max_length=50, choices=USUARIO_CHOICES)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.username

# class Propiedad(models.Model):
#     TIPO_INMUEBLE_CHOICES = (
#         ('casa', 'Casa'),
#         ('departamento', 'Departamento'),
#         ('parcela', 'Parcela'),
#     )
#     nombre = models.CharField(max_length=255)
#     descripcion = models.TextField()
#     m2_construidos = models.FloatField()
#     m2_terreno = models.FloatField()
#     num_estacionamientos = models.PositiveIntegerField()
#     num_habitaciones = models.PositiveIntegerField()
#     num_banos = models.PositiveIntegerField()
#     direccion = models.CharField(max_length=255)
#     comuna = models.CharField(max_length=100)
#     tipo_inmueble = models.CharField(max_length=50, choices=TIPO_INMUEBLE_CHOICES)
#     precio_arriendo_mensual = models.DecimalField(max_digits=10, decimal_places=2)
#     arrendador = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre
