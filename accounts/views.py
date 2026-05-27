from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import CadastroForm, PerfilForm
from .models import Usuario

def logout_view(request):
    logout(request)
    return redirect('login')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'accounts/cadastro.html', {'form': form})

@login_required
def perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado!')
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user)
    return render(request, 'accounts/perfil.html', {'form': form})

@login_required
def perfil_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'accounts/perfil_usuario.html', {'usuario': usuario})