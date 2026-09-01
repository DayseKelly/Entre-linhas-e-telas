from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form': form})


