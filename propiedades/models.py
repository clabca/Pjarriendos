from usuarios.models import PerfilUsuario  # Importa el modelo de usuario personalizado
from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class TipoPropiedad(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre  

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
#     arrendador = models.ForeignKey(PerfilUsuario, null=True, on_delete=models.CASCADE)  # Usa el modelo personalizado de usuario

    # def __str__(self):
    #     return self.nombre


class Propiedad(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_terreno = models.FloatField()
    num_estacionamientos = models.PositiveIntegerField()
    num_habitaciones = models.PositiveIntegerField()
    num_banos = models.PositiveIntegerField()
    direccion = models.CharField(max_length=255)
    comuna = models.ForeignKey(Comuna, null=True, on_delete=models.CASCADE)
    #comuna = models.CharField(max_length=100)
    tipo_propiedad = models.ForeignKey(TipoPropiedad, null=True, on_delete=models.CASCADE)
    precio_arriendo_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    arrendador = models.ForeignKey(PerfilUsuario, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

