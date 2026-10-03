from django import forms
from .models import Carta


class CartaForm(forms.ModelForm):
    class Meta:
        model = Carta
        fields = [
            'nombre',
            'posicion',
            'media',
            'club',
            'liga',
            'nacionalidad',
            'tipo_carta',
            'precio'
        ]