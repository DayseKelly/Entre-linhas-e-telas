from django.db import models

# 1. Tema ENEM
class TemaEnem(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


#2 obra
class Obra(models.Model):
    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100)
    resumo = models.TextField()
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    temas = models.ManyToManyField(TemaEnem, related_name='Obras')   

    def __str__(self):
        return self.titulo
    

#3 usuario 
class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome



#avaliacao
class Avaliacao(models.Model):
    nota = models.FloatField()
    comentario = models.TextField()
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='avaliacoes')  
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='avaliacoes') 

    def __str__(self):
        return f"Nota {self.nota} por {self.nome}"
