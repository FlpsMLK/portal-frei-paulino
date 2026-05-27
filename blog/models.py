from django.db import models
from django.utils import timezone
from accounts.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self): return self.nome

class Post(models.Model):
    STATUS = [('rascunho','Rascunho'),('publicado','Publicado')]
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(unique=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posts')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.CharField(max_length=300, blank=True, help_text='Separadas por vírgula')
    conteudo = models.TextField()
    imagem_capa = models.ImageField(upload_to='blog/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='rascunho')
    data_publicacao = models.DateTimeField(default=timezone.now)
    data_criacao = models.DateTimeField(auto_now_add=True)
    empresa = models.CharField(max_length=100, blank=True, help_text='Nome da empresa (para posts de processo seletivo)')

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self): return self.titulo

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conteudo = models.TextField()
    aprovado = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"Comentário de {self.autor} em {self.post}"
