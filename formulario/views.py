# Importando funciones necesarias de Django
from django.shortcuts import render, redirect
from django.urls import reverse

# Importando modelos y formularios definidos en la aplicación actual
from .models import investigar
from .forms import Formulario_Investigar

# Vista para llenar un formulario de investigación
def llenar_formulario(request):
    # Verificar si el formulario se está enviando mediante el método POST
    if request.method == "POST":
        # Crear una instancia del formulario con los datos recibidos
        formulario = Formulario_Investigar(request.POST)

        # Imprimir el formulario en la consola (útil para depuración)
        print(formulario)

        # Validar si el formulario es válido
        if formulario.is_valid():
            # Obtener datos limpios del formulario
            data = formulario.cleaned_data
            nombre = data["nombre_completo"]
            correo = data["correo"]
            mensaje = data["mensaje"]
            tipo_de_contacto = data["tipo_de_contacto"]
            suscripcion = data["suscripcion"]

            # Crear un objeto 'investigar' con los datos y guardarlo en la base de datos
            informacion = investigar(
                nombre_completo=nombre,
                correo=correo,
                mensaje=mensaje,
                tipo_de_contacto=tipo_de_contacto,
                suscripcion=suscripcion
            )
            informacion.save()

            # Redireccionar a la vista 'mostrar_2'
            return redirect("mostrar_2")

    else:  # Si el método no es POST (probablemente GET)
        # Crear una instancia del formulario vacío
        formulario = Formulario_Investigar()

        # Renderizar la plantilla con el formulario
        http_response = render(
            request=request,
            template_name='formularios/formulario_investigar.html',
            context={'formulario': formulario}
        )

        return http_response

# Vista para realizar una búsqueda de información en la base de datos
def buscar_informacion(request):
    # Verificar si el formulario se está enviando mediante el método POST
    if request.method == "POST":
        # Obtener el filtro de búsqueda del formulario
        filtro = request.POST["busqueda"]

        # Filtrar la información en base al nombre completo que contiene el filtro
        busqueda = investigar.objects.filter(nombre_completo__icontains=filtro)

        # Renderizar la plantilla con los resultados de la búsqueda
        http_response = render(
            request=request,
            template_name='listados/listado_filtrados.html',
            context={'busqueda': busqueda}
        )

        return http_response

    else:  # Si el método no es POST (probablemente GET)
        # Renderizar la plantilla de formulario de búsqueda
        http_response = render(
            request=request,
            template_name='formularios/formulario_busqueda.html',
            context={}
        )

        return http_response

# Vista para mostrar toda la información almacenada en la base de datos
def mostrar_informacion(request):
    # Obtener todos los registros de la tabla 'investigar'
    informacion = investigar.objects.all()

    # Renderizar la plantilla con la información obtenida
    http_response = render(
        request=request,
        template_name='listados/listado_investigar.html',
        context={'informacion': informacion}
    )

    return http_response
