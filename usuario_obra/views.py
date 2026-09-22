from django.shortcuts import get_object_or_404, render, redirect
from .models import UsuarioObra
from .forms import UsuarioObraForm
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('usuario_obra.view_usuarioobra', raise_exception=True)
def listar_usuario_obras(request):
    registros = UsuarioObra.objects.all()
    return render(request, 'lista_usuario_obra.html', {'usuario_obras': registros})


@login_required
@permission_required('usuario_obra.add_usuarioobra', raise_exception=True)
def criar_usuario_obra(request):
    if request.method == 'POST':
        form = UsuarioObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuario_obras')
    else:
        form = UsuarioObraForm()
    return render(request, 'form_usuario_obra.html', {'form': form})


@login_required
@permission_required('usuario_obra.view_usuarioobra', raise_exception=True)
def detalhe_usuario_obra(request, id):
    registro = get_object_or_404(UsuarioObra, id=id)
    return render(request, 'detalhe_usuario_obra.html', {'registro': registro})


@login_required
@permission_required('usuario_obra.change_usuarioobra', raise_exception=True)
def editar_usuario_obra(request, id):
    registro = get_object_or_404(UsuarioObra, id=id)

    if request.method == 'POST':
        form = UsuarioObraForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('detalhe_usuario_obra', id=registro.id)
    else:
        form = UsuarioObraForm(instance=registro)

    return render(request, 'form_usuario_obra.html', {
        'form': form,
        'titulo_pagina': 'Editar relação usuário-obra',
    })


@login_required
@permission_required('usuario_obra.delete_usuarioobra', raise_exception=True)
def excluir_usuario_obra(request, id):
    registro = get_object_or_404(UsuarioObra, id=id)

    if request.method == 'POST':
        registro.delete()
        return redirect('listar_usuario_obras')

    return render(request, 'excluir_usuario_obra.html', {'registro': registro})