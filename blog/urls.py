from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('busca/', views.busca_posts, name='busca_posts'),
    path('novo/', views.criar_post, name='criar_post'),
    path('<slug:slug>/', views.detalhe_post, name='detalhe_post'),
    path('<slug:slug>/editar/', views.editar_post, name='editar_post'),
]
