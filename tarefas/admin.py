from django.contrib import admin
from .models import Tarefa, Entrega

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'professor', 'turma', 'prazo', 'status')

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'tarefa', 'data_entrega', 'nota')
