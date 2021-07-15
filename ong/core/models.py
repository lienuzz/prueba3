from django.db import models
from django.db.models.base import Model

# Create your models here.
#aqui se definen las clases
class categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre de la Categoria")
    def __str__(self):
        return self.nombreCategoria

class Pintura(models.Model):
    idPintura = models.IntegerField(primary_key=True, verbose_name="IDpintura")
    nombre = models.CharField(max_length=20, verbose_name="Nombre pintura")
    autor = models.CharField(max_length=50, null=True, blank=True, verbose_name="Autor")
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre








