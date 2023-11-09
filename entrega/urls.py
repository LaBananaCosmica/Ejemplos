# Importando la clase 'admin' de Django y la función de ruta (path)
from django.contrib import admin 
from django.urls import path, include

# Definiendo patrones de URL para el proyecto principal
urlpatterns = [
    # Ruta para acceder al panel de administración de Django
    path("admin/", admin.site.urls),

    # Ruta para incluir los patrones de URL de la aplicación 'formulario'
    path("", include("formulario.urls")),
]
