from django import forms
from django.forms import ModelForm, fields
from .models import Pintura


class PinturaForm(ModelForm):
    class Meta:
        #OBJETO QUE VAMOS A CONSULTAR
        model = Pintura
        #QUE CAMPOS VAMOS A TRAER
        fields = ['idPintura', 'nombre', 'autor', 'categoria']