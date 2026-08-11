from django.db import models
from temas.models import TemaEnem  # Importa do app temas

class Obra(models.Model):
    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100)
    resumo = models.TextField()
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    temas = models.ManyToManyField(TemaEnem, related_name='obras')

    def __str__(self):
        return self.titulo