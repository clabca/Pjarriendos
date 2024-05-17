import os
import django

# Establece la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pjarriendos.settings')

# Configura Django
django.setup()




# Importa los modelos necesarios
from propiedades.models import Propiedad, Comuna, Region

# Realiza la consulta para obtener los inmuebles por comuna
def consultar_inmuebles_por_regiones():
    # Realiza la consulta para obtener los inmuebles agrupados por regiones
    regiones_con_inmuebles = {}
    for region in Region.objects.all():
        inmuebles_por_region = Propiedad.objects.filter(comuna__region=region)
        if inmuebles_por_region.exists():
            regiones_con_inmuebles[region.nombre] = list(inmuebles_por_region.values_list('nombre', flat=True))

    # Guarda los resultados en un archivo de texto
    with open('inmuebles_por_regiones.txt', 'w') as file:
        for region, inmuebles in regiones_con_inmuebles.items():
            file.write(f'Región: {region}\n')
            file.write('Inmuebles:\n')
            for inmueble in inmuebles:
                file.write(f'- {inmueble}\n')
            file.write('\n')

# Llama a la función para ejecutarla
consultar_inmuebles_por_regiones()