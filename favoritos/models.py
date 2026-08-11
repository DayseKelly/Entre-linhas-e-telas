from django.db import models
from usuarios.models import Usuario
from obras.models import Obra

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='favoritos')
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='favoritados')

    def __str__(self):
        return f"{self.usuario.nome} - {self.obra.titulo}"