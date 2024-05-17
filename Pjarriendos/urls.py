"""
URL configuration for Pjarriendos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from propiedades import views as pv
from usuarios import views as uv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # Incluir las URLs de la aplicación usuarios
    path('propiedades/', include('propiedades.urls')),  # Incluir las URLs de la aplicación propiedades 
    path('accounts/', include('django.contrib.auth.urls')),  # Incluir las URLs de la aplicación django.contrib.auth
    path('', pv.welcome, name='welcome'),
    path('register/', uv.registro_usuario, name='register'),
    path('login/', uv.login_view, name='login'),
    path('logout/', uv.cerrar_sesion, name='logout'),
    path('arrendatario_home/', pv.arrendatario_home, name='arrendatario_home'),
    path('arrendador_home/', pv.arrendador_home, name='arrendador_home'),

]