from django import forms
from .models import Propiedad

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_terreno', 'num_estacionamientos', 'num_habitaciones', 'num_banos', 'direccion', 'comuna', 'tipo_propiedad', 'precio_arriendo_mensual']
