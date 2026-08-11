from django.db import models
from usuarios.models import Usuario  # Importa do app usuarios
from obras.models import Obra        # Importa do app obras

class Avaliacao(models.Model):
    nota = models.FloatField()
    comentario = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='avaliacoes')
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='avaliacoes')

    def __str__(self):
        return f"Nota {self.nota} por {self.usuario.nome}"