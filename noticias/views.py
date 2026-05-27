from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Noticia, Evento
from .forms import NoticiaForm, EventoForm
from blog.models import Post
from tarefas.models import Tarefa

def home(request):
    noticias_destaque = Noticia.objects.filter(destaque=True)[:3]
    noticias_recentes = Noticia.objects.all()[:6]
    eventos_proximos = Evento.objects.filter(data_inicio__gte=timezone.now())[:5]
    posts_recentes = Post.objects.filter(status='publicado')[:3]
    return render(request, 'home.html', {
        'noticias_destaque': noticias_destaque,
        'noticias_recentes': noticias_recentes,
        'eventos_proximos': eventos_proximos,
        'posts_recentes': posts_recentes,
    })

def lista_noticias(request):
    categoria = request.GET.get('categoria')
    noticias = Noticia.objects.all()
    if categoria:
        noticias = noticias.filter(categoria=categoria)
    return render(request, 'noticias/lista.html', {'noticias': noticias, 'categoria': categoria})

def detalhe_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})

def lista_eventos(request):
    eventos = Evento.objects.filter(data_inicio__gte=timezone.now())
    return render(request, 'noticias/eventos.html', {'eventos': eventos})

@login_required
def criar_noticia(request):
    if not request.user.is_professor():
        return redirect('home')
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            n = form.save(commit=False)
            n.autor = request.user
            n.save()
            messages.success(request, 'Notícia publicada!')
            return redirect('detalhe_noticia', pk=n.pk)
    else:
        form = NoticiaForm()
    return render(request, 'noticias/form.html', {'form': form, 'titulo': 'Nova Notícia'})

@login_required
def criar_evento(request):
    if not request.user.is_professor():
        return redirect('home')
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.criado_por = request.user
            e.save()
            messages.success(request, 'Evento criado!')
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'noticias/form.html', {'form': form, 'titulo': 'Novo Evento'})
