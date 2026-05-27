from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Post, Categoria, Comentario
from .forms import PostForm, ComentarioForm, BuscaForm

def lista_posts(request):
    posts = Post.objects.filter(status='publicado')
    categoria_slug = request.GET.get('categoria')
    empresa = request.GET.get('empresa')
    if categoria_slug:
        posts = posts.filter(categoria__slug=categoria_slug)
    if empresa:
        posts = posts.filter(empresa__icontains=empresa)
    categorias = Categoria.objects.all()
    return render(request, 'blog/lista.html', {'posts': posts, 'categorias': categorias})

def detalhe_post(request, slug):
    post = get_object_or_404(Post, slug=slug, status='publicado')
    comentarios = post.comentarios.filter(aprovado=True)
    form = ComentarioForm()
    if request.method == 'POST' and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.post = post
            c.autor = request.user
            c.save()
            messages.info(request, 'Comentário enviado para moderação.')
            return redirect('detalhe_post', slug=slug)
    return render(request, 'blog/detalhe.html', {'post': post, 'comentarios': comentarios, 'form': form})

def busca_posts(request):
    form = BuscaForm(request.GET)
    posts = []
    q = request.GET.get('q', '')
    if q:
        posts = Post.objects.filter(
            status='publicado'
        ).filter(Q(titulo__icontains=q) | Q(conteudo__icontains=q) | Q(tags__icontains=q) | Q(empresa__icontains=q))
    return render(request, 'blog/busca.html', {'posts': posts, 'q': q, 'form': form})

@login_required
def criar_post(request):
    if not request.user.is_professor():
        messages.error(request, 'Apenas professores podem criar posts.')
        return redirect('lista_posts')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, 'Post criado com sucesso!')
            return redirect('detalhe_post', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/form_post.html', {'form': form, 'titulo': 'Novo Post'})

@login_required
def editar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.autor != request.user and not request.user.is_staff:
        messages.error(request, 'Sem permissão.')
        return redirect('lista_posts')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post atualizado!')
            return redirect('detalhe_post', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/form_post.html', {'form': form, 'titulo': 'Editar Post', 'post': post})
