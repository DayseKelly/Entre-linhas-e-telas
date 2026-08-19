from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.nome} - {self.cidade}/{self.estado}"