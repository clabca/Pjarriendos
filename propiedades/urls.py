from django.urls import path
from propiedades import views

urlpatterns = [
    path('', views.listar_propiedades, name='listar_propiedades'),
    path('<int:propiedad_id>/', views.detalle_propiedad, name='detalle_propiedad'),
    path('crear/', views.crear_propiedad, name='crear_propiedad'),
    path('<int:propiedad_id>/editar/', views.editar_propiedad, name='editar_propiedad'),
    path('<int:propiedad_id>/eliminar/', views.eliminar_propiedad, name='eliminar_propiedad'),
    path('propiedades_disponibles/', views.listar_propiedades_disponibles, name='propiedades_disponibles'),


]
