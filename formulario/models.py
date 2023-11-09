# Importando la clase 'models' de Django
from django.db import models

# Opciones para el campo 'tipo_de_contacto'
options = [
    [0, "Número de celular"],
    [1, "Correo electrónico"]
]

# Modelo 'investigar' para almacenar información de contacto
class investigar(models.Model):
    # Campos del modelo
    nombre_completo = models.CharField(max_length=100, verbose_name="Nombre_Apellido")
    correo = models.EmailField(verbose_name="Correo electrónico")
    mensaje = models.TextField(verbose_name="Mensaje")
    tipo_de_contacto = models.IntegerField(choices=options, verbose_name="Tipo de contacto")
    suscripcion = models.BooleanField(default=False, verbose_name="Suscribirme a correos informativos")

    # Método que devuelve una representación de cadena del objeto
    def __str__(self):
        return f"{self.nombre_completo}, {self.correo}, {self.mensaje}, {self.tipo_de_contacto}"

# Clase 'Personas' (actualmente vacía, ¿quizás sea un trabajo en progreso?)
class Personas(models.Model):
    pass
