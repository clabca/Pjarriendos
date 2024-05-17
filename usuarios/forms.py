from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PerfilUsuario
#from usuarios.models import PerfilUsuario  # Importa tu modelo de usuario personalizado

class RegistroForm(UserCreationForm):
    TIPO_USUARIO_CHOICES = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )
    tipo_usuario = forms.ChoiceField(choices=TIPO_USUARIO_CHOICES)
    rut = forms.CharField(max_length=12)
    telefono = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=255)

    class Meta:
        model = PerfilUsuario  # Utiliza tu modelo de usuario personalizado
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', 'tipo_usuario', 'rut', 'telefono', 'direccion')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos'
        }
        help_texts = {
            'username': '',
                  }


class ActualizacionForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ( 'first_name','last_name', 'email', 'rut', 'telefono', 'direccion')

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos'
        }