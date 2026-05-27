from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Canal, Mensagem
from .forms import CanalForm

@login_required
def lista_canais(request):
    canais_publicos = Canal.objects.filter(tipo='publico')
    meus_canais = request.user.canais.all()
    return render(request, 'chat/lista.html', {'canais_publicos': canais_publicos, 'meus_canais': meus_canais})

@login_required
def sala_chat(request, canal_id):
    canal = get_object_or_404(Canal, pk=canal_id)
    if canal.tipo == 'privado' and request.user not in canal.membros.all() and canal.criado_por != request.user:
        messages.error(request, 'Acesso restrito a este canal.')
        return redirect('lista_canais')
    mensagens = canal.mensagens.select_related('remetente').all()[:100]
    canal.membros.add(request.user)
    return render(request, 'chat/sala.html', {'canal': canal, 'mensagens': mensagens})

@login_required
def criar_canal(request):
    if not request.user.is_professor():
        messages.error(request, 'Apenas professores podem criar canais.')
        return redirect('lista_canais')
    if request.method == 'POST':
        form = CanalForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.criado_por = request.user
            c.save()
            c.membros.add(request.user)
            messages.success(request, 'Canal criado!')
            return redirect('sala_chat', canal_id=c.pk)
    else:
        form = CanalForm()
    return render(request, 'chat/criar_canal.html', {'form': form})
