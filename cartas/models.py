from django.db import models


class Carta(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=10)
    media = models.IntegerField()
    club = models.CharField(max_length=100)
    liga = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    tipo_carta = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre