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
 return render(request, 'obras/criar_obra.html', {'form': form})