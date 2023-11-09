# Importando clases necesarias de Django
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Importando el modelo 'Investigar' definido en el archivo models.py
from .models import Investigar

# Definiendo un formulario basado en el modelo 'Investigar'
class Formulario_Investigar(forms.ModelForm):
    class Meta:
        # Especificando el modelo asociado al formulario
        model = Investigar

        # Especificando que se deben incluir todos los campos del modelo en el formulario
        fields = "__all__"
