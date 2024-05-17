from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import PerfilUsuario

class PerfilUsuarioAdmin(UserAdmin):
    model = PerfilUsuario
    list_display = ['username', 'email', 'tipo_usuario', 'rut', 'telefono', 'direccion']

admin.site.register(PerfilUsuario)
