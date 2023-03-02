from django.forms import ModelForm
from .models import Receta
from django import forms


# Formulario para añadir un nuevo libro
class recetaForm(ModelForm):
    class Meta: 
        model = Receta
        fields = ['nombre', 'preparación', 'foto']
        
        
        



