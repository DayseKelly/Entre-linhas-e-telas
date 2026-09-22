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
   return redirect('listar_obras')
 else:

  messages.error(request, 'Erro ao criar obra.')
  form = ObraForm()
 return render(request, 'obras/form_obra.html', {'form': form})

@login_required
@permission_required('obras.view_obra')
def detalhe_obra(request, id):
    obra = get_object_or_404(Obra, id=id)
    return render(request, 'obras/detalhe_obra.html', {'obra': obra})