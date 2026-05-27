from django.contrib import admin
from .models import Canal, Mensagem

@admin.register(Canal)
class CanalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'criado_por', 'data_criacao')

admin.site.register(Mensagem)
