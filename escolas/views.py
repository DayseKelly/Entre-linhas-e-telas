from django.shortcuts import render, redirect
from .models import Escola
from .forms import EscolaForm
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('escolas.view_escolas')

def listar_escolas(request):
    escolas = Escola.objects.all()
    return render(request, 'escolas/lista_escolas.html', {'escolas': escolas})


@login_required
@permission_required('escolas.add_escolas')

def criar_escola(request):
    if request.method == 'POST':
        form = EscolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_escolas')
    else:
        form = EscolaForm()
    return render(request, 'escolas/form_escola.html', {'form': form})

# Create your views here.
