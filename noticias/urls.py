from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_noticias, name='lista_noticias'),
    path('nova/', views.criar_noticia, name='criar_noticia'),
    path('<int:pk>/', views.detalhe_noticia, name='detalhe_noticia'),
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/novo/', views.criar_evento, name='criar_evento'),
]
