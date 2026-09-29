from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.forms import AuthenticationForm       
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required

User = get_user_model()

@login_required
@permission_required("usuarios.view_usuario", raise_exception=True)
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})


@login_required
def minha_area(request):
    try:
        perfil = request.user.perfil
    except Usuario.DoesNotExist:
        perfil = None
    return render(request, 'minha_area.html', {
        'perfil': perfil,
        'favoritos_total': request.user.minhas_obras.filter(favorito=True).count(),
        'comentarios_total': request.user.avaliacoes.count(),
        'active_tab': 'inicio',
    })


@login_required
@permission_required("usuarios.add_usuario", raise_exception=True)
def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso.')
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'form_usuarios.html', {'form': form})


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
            usuario.user.username = form.cleaned_data['username']
            usuario.user.save(update_fields=['username'])
            form.save()
            messages.success(request, 'Usuário editado com sucesso.')
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
        usuario.user.delete()
        messages.success(request, 'Usuário excluído com sucesso.')
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

    form.fields['username'].label = 'Usuário'
    form.fields['username'].widget.attrs.update({'placeholder': 'Seu usuário', 'autocomplete': 'username'})
    form.fields['password'].label = 'Senha'
    form.fields['password'].widget.attrs.update({'placeholder': 'Sua senha', 'autocomplete': 'current-password'})
    form.error_messages['invalid_login'] = 'Usuário ou senha incorretos.'
    
    return render(request, 'login.html', {'form': form})

@login_required
def fazer_logout(request):
    logout(request)
    return redirect('login')


