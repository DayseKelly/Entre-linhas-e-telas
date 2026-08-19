from django.db import models
from django.contrib.auth.models import User
from escolas.models import Escola

class Usuario(models.Model):
    # Ligação de herança/perfil com o User nativo do Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    
    data_nasc = models.DateField()
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    # FK_escola (1:N - uma escola para vários usuários)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='usuarios')

    def __str__(self):
        return self.user