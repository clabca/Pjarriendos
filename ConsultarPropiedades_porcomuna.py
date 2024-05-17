import os
import django

# Establece la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pjarriendos.settings')

# Configura Django
django.setup()




# Importa los modelos necesarios
from propiedades.models import Propiedad, Comuna

# Realiza la consulta para obtener los inmuebles por comuna
def consultar_inmuebles_por_comuna():
    try:
        # Abre el archivo de texto para escribir los resultados
        with open('inmuebles_por_comuna.txt', 'w') as archivo:
            # Obtiene todas las comunas
            comunas = Comuna.objects.all()
            for comuna in comunas:
                # Obtiene los inmuebles para la comuna actual
                inmuebles = Propiedad.objects.filter(comuna=comuna)
                # Escribe los resultados en el archivo de texto
                archivo.write(f'Comuna: {comuna.nombre}\n')
                archivo.write('----------------------------------------\n')
                for inmueble in inmuebles:
                    archivo.write(f'Nombre: {inmueble.nombre}\n')
                    archivo.write(f'Descripción: {inmueble.descripcion}\n\n')
                archivo.write('\n')
            print('Consulta exitosa. Los resultados se han guardado en "inmuebles_por_comuna.txt".')
    except Exception as e:
        print(f'Ocurrió un error al ejecutar la consulta: {e}')

# Ejecuta la función para consultar los inmuebles por comuna y guardar los resultados en un archivo de texto
consultar_inmuebles_por_comuna()
