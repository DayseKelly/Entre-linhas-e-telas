from django.shortcuts import get_object_or_404, render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.forms import AuthenticationForm       
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required("usuarios.view_usuario", raise_exception=True)
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


@login_required
@permission_required("usuarios.add_usuario", raise_exception=True)
def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form': form})


@login_required
@permission_required("usuarios.view_usuario", raise_exception=True)
def detalhe_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, 'detalhe_usuario.html', {'usuario': usuario})


@login_required
@permission_required("usuarios.change_usuario", raise_exception=True)
def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('detalhe_usuario', id=usuario.id)
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'form_usuarios.html', {
        'form': form,
        'titulo_pagina': 'Editar usuário',
    })


@login_required
@permission_required("usuarios.delete_usuario", raise_exception=True)
def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')

    return render(request, 'excluir_usuario.html', {'usuario': usuario})

def fazer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redireciona para a página principal (ex: lista de obras)
            return redirect('listar_obras')
    else:
        form = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def fazer_logout(request):
    logout(request)
    return redirect('login')


