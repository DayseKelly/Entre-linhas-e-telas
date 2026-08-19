from django.db import models
from usuarios.models import Usuario
from obras.models import Obra

class UsuarioObra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='minhas_obras')
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='usuarios_interagiram')
    
    # Flags Booleanas (true or false) do diagrama
    favorito = models.BooleanField(default=False)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.user.username} -Obra: {self.obra.titulo}"