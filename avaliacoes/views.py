from django.shortcuts import render, redirect
from .models import Avaliacao
from .forms import AvaliacaoForm
from django.contrib.auth.decorators import login_required, permission_required

def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'avaliacoes/lista_avaliacoes.html', {'avaliacoes': avaliacoes})

@login_required(login_url='login')
@permission_required('avaliacoes.add_avaliacao', login_url='login', raise_exception=True)

def criar_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_avaliacoes')
    else:
        form = AvaliacaoForm()
    return render(request, 'avaliacoes/form_avaliacao.html', {'form': form})