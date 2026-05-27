from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_canais, name='lista_canais'),
    path('novo/', views.criar_canal, name='criar_canal'),
    path('<int:canal_id>/', views.sala_chat, name='sala_chat'),
]
