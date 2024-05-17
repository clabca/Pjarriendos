from django.shortcuts import render, redirect, get_object_or_404
from .models import Propiedad
from .forms import PropiedadForm
from usuarios import views

def listar_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'propiedades/listar_propiedades.html', {'propiedades': propiedades})

def detalle_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, pk=propiedad_id)
    return render(request, 'propiedades/detalle_propiedad.html', {'propiedad': propiedad})

def crear_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_propiedades')
    else:
        form = PropiedadForm()
    return render(request, 'propiedades/crear_propiedad.html', {'form': form})

def editar_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, pk=propiedad_id)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
            return redirect('listar_propiedades')
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'propiedades/editar_propiedad.html', {'form': form})

def eliminar_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, pk=propiedad_id)
    if request.method == 'POST':
        propiedad.delete()
        return redirect('listar_propiedades')
    return render(request, 'propiedades/eliminar_propiedad.html', {'propiedad': propiedad})




def welcome(request):
    return render(request, 'propiedades/bienvenido.html')

def arrendatario_home(request):
    return render(request, 'propiedades/arrendatario_home.html')

def arrendador_home(request):
    return render(request, 'usuarios/perfil_usuario_arrendador.html')

def listar_propiedades_disponibles(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'propiedades/arrendatario_propiedades_disponibles.html', {'propiedades': propiedades})
