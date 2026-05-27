from django.contrib import admin
from .models import Noticia, Evento

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'data_publicacao', 'destaque')
    list_filter = ('categoria', 'destaque')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_inicio', 'local')
    list_filter = ('categoria',)
