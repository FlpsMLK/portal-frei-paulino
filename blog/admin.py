from django.contrib import admin
from .models import Post, Categoria, Comentario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'status', 'data_publicacao')
    list_filter = ('status', 'categoria')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'conteudo', 'tags')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'post', 'aprovado', 'data')
    list_filter = ('aprovado',)
    actions = ['aprovar']

    def aprovar(self, request, queryset):
        queryset.update(aprovado=True)
    aprovar.short_description = "Aprovar comentários selecionados"
