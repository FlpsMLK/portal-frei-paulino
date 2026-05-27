from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('nova/', views.criar_tarefa, name='criar_tarefa'),
    path('<int:pk>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    path('entrega/<int:pk>/avaliar/', views.avaliar_entrega, name='avaliar_entrega'),
]
