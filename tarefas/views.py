from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tarefa, Entrega
from .forms import TarefaForm, EntregaForm, FeedbackForm

@login_required
def lista_tarefas(request):
    user = request.user
    if user.is_professor():
        tarefas = Tarefa.objects.filter(professor=user)
    else:
        tarefas = Tarefa.objects.filter(turma__in=[user.turma, 'todas'])
    minhas_entregas = {e.tarefa_id for e in Entrega.objects.filter(aluno=user)}
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas, 'minhas_entregas': minhas_entregas})

@login_required
def detalhe_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    entrega_existente = None
    form = None
    entregas = None
    if request.user.is_professor():
        entregas = tarefa.entregas.select_related('aluno').all()
    else:
        try:
            entrega_existente = Entrega.objects.get(tarefa=tarefa, aluno=request.user)
        except Entrega.DoesNotExist:
            pass
        if not entrega_existente and not tarefa.prazo_expirado():
            form = EntregaForm()
            if request.method == 'POST':
                form = EntregaForm(request.POST, request.FILES)
                if form.is_valid():
                    e = form.save(commit=False)
                    e.tarefa = tarefa
                    e.aluno = request.user
                    e.save()
                    messages.success(request, 'Tarefa entregue com sucesso!')
                    return redirect('detalhe_tarefa', pk=pk)
    return render(request, 'tarefas/detalhe.html', {
        'tarefa': tarefa, 'form': form, 'entrega_existente': entrega_existente, 'entregas': entregas
    })

@login_required
def criar_tarefa(request):
    if not request.user.is_professor():
        return redirect('lista_tarefas')
    if request.method == 'POST':
        form = TarefaForm(request.POST, request.FILES)
        if form.is_valid():
            t = form.save(commit=False)
            t.professor = request.user
            t.save()
            messages.success(request, 'Tarefa criada e publicada!')
            return redirect('detalhe_tarefa', pk=t.pk)
    else:
        form = TarefaForm()
    return render(request, 'tarefas/form.html', {'form': form})

@login_required
def avaliar_entrega(request, pk):
    entrega = get_object_or_404(Entrega, pk=pk)
    if entrega.tarefa.professor != request.user:
        return redirect('lista_tarefas')
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=entrega)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avaliação salva!')
            return redirect('detalhe_tarefa', pk=entrega.tarefa.pk)
    else:
        form = FeedbackForm(instance=entrega)
    return render(request, 'tarefas/avaliar.html', {'form': form, 'entrega': entrega})
