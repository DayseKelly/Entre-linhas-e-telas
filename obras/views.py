from django.shortcuts import render, redirect
from .models import Obra
from .forms import ObraForm

def listar_obras(request):
 obras = Obra.objects.all()
 return render(request, 'obras/lista_obras.html', {'obras': obras})

def criar_obra(request):
 if request.method == 'POST':
  form = ObraForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return redirect('listar_obras')
 else:
  form = ObraForm()
 return render(request, 'obras/form_obra.html', {'form': form})

 def detalhe_obra(request, id):
    # O get_object_or_404 busca a obra pelo ID no banco de dados.
    # Se o ID não existir (ex: /obras/9999/), ele abre uma página de erro 404 em vez de quebrar o site.
    obra = get_object_or_404(Obra, id=id)
    
    return render(request, 'obras/detalhe_obra.html', {'obra': obra})