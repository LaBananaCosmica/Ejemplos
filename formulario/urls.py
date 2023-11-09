# Importando la función de ruta (path) de Django
from django.urls import path

# Importando las vistas definidas en el archivo views.py
from .views import llenar_formulario, mostrar_informacion, buscar_informacion

# Definición de patrones de URL para la aplicación
urlpatterns = [
    # Ruta para acceder al formulario de investigación
    path("formulario_investigar/", llenar_formulario, name="llenar_formulario"),

    # Ruta para mostrar la información de investigación almacenada
    path("mostrar_investigar/", mostrar_informacion, name="mostrar_2"),

    # Ruta para realizar búsquedas en la información almacenada
    path("busqueda/", buscar_informacion, name="filtrados"),
]
