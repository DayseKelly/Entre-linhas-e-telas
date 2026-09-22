from django.shortcuts import get_object_or_404, render, redirect
from .models import Avaliacao
from .forms import AvaliacaoForm
from django.contrib.auth.decorators import login_required, permission_required




@login_required
@permission_required('avaliacoes.view_avaliacao', raise_exception=True)
def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'listar_avaliacoes.html', {'avaliacoes': avaliacoes})

@login_required
@permission_required('avaliacoes.add_avaliacao', raise_exception=True)
def criar_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_avaliacoes')
    else:
        form = AvaliacaoForm()
    return render(request, 'forms_avaliacoes.html', {'form': form})


@login_required
@permission_required('avaliacoes.view_avaliacao', raise_exception=True)
def detalhe_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)
    return render(request, 'detalhe_avaliacao.html', {'avaliacao': avaliacao})


@login_required
@permission_required('avaliacoes.change_avaliacao', raise_exception=True)
def editar_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('detalhe_avaliacao', id=avaliacao.id)
    else:
        form = AvaliacaoForm(instance=avaliacao)

    return render(request, 'forms_avaliacoes.html', {
        'form': form,
        'titulo_pagina': 'Editar avaliação',
    })


@login_required
@permission_required('avaliacoes.delete_avaliacao', raise_exception=True)
def excluir_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)

    if request.method == 'POST':
        avaliacao.delete()
        return redirect('listar_avaliacoes')

    return render(request, 'excluir_avaliacao.html', {'avaliacao': avaliacao})