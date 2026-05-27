from django.db import models
from accounts.models import Usuario

class Canal(models.Model):
    TIPO_CHOICES = [('publico','Público'),('privado','Privado')]
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='publico')
    criado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='canais_criados')
    membros = models.ManyToManyField(Usuario, related_name='canais', blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.nome

class Mensagem(models.Model):
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE, related_name='mensagens', null=True, blank=True)
    remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='mensagens_recebidas')
    conteudo = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    class Meta:
        ordering = ['data_hora']

    def __str__(self):
        return f"{self.remetente}: {self.conteudo[:50]}"
