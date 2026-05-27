from django.db import models
from django.utils import timezone
from accounts.models import Usuario

class Noticia(models.Model):
    CATEGORIA_CHOICES = [
        ('geral', 'Geral'),
        ('academico', 'Acadêmico'),
        ('cultural', 'Cultural'),
        ('esportivo', 'Esportivo'),
        ('comunicado', 'Comunicado'),
    ]
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='geral')
    data_publicacao = models.DateTimeField(default=timezone.now)
    destaque = models.BooleanField(default=False)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self): return self.titulo

class Evento(models.Model):
    CATEGORIA_CHOICES = [
        ('academico', 'Acadêmico'),
        ('cultural', 'Cultural'),
        ('esportivo', 'Esportivo'),
        ('outro', 'Outro'),
    ]
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(blank=True, null=True)
    local = models.CharField(max_length=200, blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='academico')
    criado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        ordering = ['data_inicio']

    def __str__(self): return self.titulo
