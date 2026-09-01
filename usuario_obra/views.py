from django.shortcuts import render, redirect
from .models import UsuarioObra
from .forms import UsuarioObraForm

def listar_usuario_obras(request):
    registros = UsuarioObra.objects.all()
    return render(request, 'usuario_obra/lista_usuario_obras.html', {'registros': registros})

def criar_usuario_obra(request):
    if request.method == 'POST':
        form = UsuarioObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuario_obras')
    else:
        form = UsuarioObraForm()
    return render(request, 'usuario_obra/form_usuario_obra.html', {'form': form})