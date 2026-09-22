from django.shortcuts import get_object_or_404, render, redirect
from .models import Obra
from .forms import ObraForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages


@login_required
@permission_required('obras.view_obra')
def listar_obras(request):
 obras = Obra.objects.all()
 return render(request, 'obras/lista_obras.html', {'obras': obras})

@login_required
@permission_required('obras.add_obra')
def criar_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Obra cadastrada com sucesso.')
            return redirect('listar_obras')
    else:
        form = ObraForm()

    return render(request, 'obras/form_obra.html', {
        'form': form,
        'titulo_pagina': 'Cadastrar obra',
    })


  
@login_required
@permission_required('obras.view_obra')
def detalhe_obra(request, id):
    obra = get_object_or_404(Obra, id=id)
    return render(request, 'obras/detalhe_obra.html', {'obra': obra})

@login_required
@permission_required('obras.change_obra', raise_exception=True)
def editar_obra(request, id):
    obra = get_object_or_404(Obra, id=id)

    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES, instance=obra)

        if form.is_valid():
            form.save()
            messages.success(request, 'Obra editada com sucesso.')
            return redirect('detalhe_obra', id=obra.id)
    else:
        form = ObraForm(instance=obra)

    return render(request, 'obras/form_obra.html', {
        'form': form,
         'titulo_pagina': 'Editar obra',
        'obra': obra,
    })
@login_required
@permission_required('obras.delete_obra', raise_exception=True)
def excluir_obra(request, id):
    obra = get_object_or_404(Obra, id=id)

    if request.method == 'POST':
        obra.delete()
        messages.success(request, 'Obra excluída com sucesso.')
        return redirect('listar_obras')

    return render(request, 'obras/excluir.html', {
        'obra': obra,
    })