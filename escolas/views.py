from django.shortcuts import render, redirect
from .models import Escola
from .forms import EscolaForm

def listar_escolas(request):
    escolas = Escola.objects.all()
    return render(request, 'escolas/lista_escolas.html', {'escolas': escolas})

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
