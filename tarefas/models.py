from django.db import models
from django.utils import timezone
from accounts.models import Usuario

class Tarefa(models.Model):
    STATUS_CHOICES = [('aberta','Aberta'),('encerrada','Encerrada')]
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tarefas_criadas')
    turma = models.CharField(max_length=50, help_text='Ex: 3A, ou "todas"')
    data_criacao = models.DateTimeField(auto_now_add=True)
    prazo = models.DateTimeField()
    arquivo_enunciado = models.FileField(upload_to='tarefas/enunciados/', blank=True, null=True)
    criterios = models.TextField(blank=True, help_text='Critérios de avaliação')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberta')

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self): return self.titulo

    def prazo_expirado(self):
        return timezone.now() > self.prazo

class Entrega(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='entregas')
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='entregas')
    arquivo = models.FileField(upload_to='tarefas/entregas/')
    comentario = models.TextField(blank=True)
    data_entrega = models.DateTimeField(auto_now_add=True)
    nota = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    feedback = models.TextField(blank=True)

    class Meta:
        unique_together = ('tarefa', 'aluno')

    def __str__(self): return f"{self.aluno} -> {self.tarefa}"
