from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, ActualizacionForm
from .models import PerfilUsuario
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Crear una instancia de PerfilUsuario con los datos del formulario
            perfil_usuario = form.save(commit=False)
            # Agregar el tipo de usuario a partir de los datos del formulario
            perfil_usuario.tipo_usuario = form.cleaned_data['tipo_usuario']
            # Guardar el perfil de usuario en la base de datos
            perfil_usuario.save()
            # Redirigir al usuario a la página de perfil
            return redirect('welcome')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro_usuario.html', {'form': form})




@login_required
def actualizar_usuario(request):
    perfil = request.user
    if request.method == 'POST':
        form = ActualizacionForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ActualizacionForm(instance=perfil)
    return render(request, 'usuarios/actualizar_usuario.html', {'form': form})

@login_required
def actualizar_usuario_arrendador(request):
    perfil = request.user
    if request.method == 'POST':
        form = ActualizacionForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil_arrendador')
    else:
        form = ActualizacionForm(instance=perfil)
    return render(request, 'usuarios/actualizar_usuario_arrendador.html', {'form': form})

@login_required
def perfil_usuario(request):
    return render(request, 'usuarios/perfil_usuario.html')
@login_required
def perfil_usuario_arrendador(request):
    return render(request, 'usuarios/perfil_usuario_arrendador.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('welcome')  # Cambia 'pagina_de_inicio' por la URL a la que deseas redirigir después de cerrar sesión


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('welcome23.html')  # Redirecciona al usuario a la página de bienvenida
#         else:
#             messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
#     return render(request, 'login2.html')



# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)  # Aquí solo se pasa la solicitud como argumento
#             next_url = request.POST.get('next', '/')
#             return redirect(next_url)
#         else:
#             # Manejar inicio de sesión inválido
#             pass
#     else:
#         next_url = request.GET.get('next', '/')
#         return render(request, 'registration/login.html', {'next_url': next_url})       


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         # Resto del código para manejar el formulario de inicio de sesión
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.tipo_usuario == 'arrendador':
                    return redirect('arrendador_home')  # Redirige al home del arrendador
                elif user.tipo_usuario == 'arrendatario':
                    return redirect('arrendatario_home')  # Redirige al home del arrendatario
                else:
                    return redirect('listar_propiedades')  # Redirige a la página inicial por defecto
                #return redirect('listar_propiedades')  # Redirigir a la página de inicio después del inicio de sesión exitoso
            else:
                # Manejar el caso en que la autenticación falla
                pass
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

