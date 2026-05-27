from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('admin', 'Administrador'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='aluno')
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    turma = models.CharField(max_length=50, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def is_professor(self):
        return self.tipo in ('professor', 'admin')

    def is_aluno(self):
        return self.tipo == 'aluno'

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_tipo_display()})"
