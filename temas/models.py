from django.db import models

class TemaEnem(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome