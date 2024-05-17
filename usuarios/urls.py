from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('actualizar/', views.actualizar_usuario, name='actualizar'),
    path('actualizararrendador/', views.actualizar_usuario_arrendador, name='actualizararrendador'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('perfil_arrendador/', views.perfil_usuario_arrendador, name='perfil_arrendador'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    
]