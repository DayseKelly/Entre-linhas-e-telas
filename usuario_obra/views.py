from django.shortcuts import render, redirect
from .models import UsuarioObra
from .forms import UsuarioObraForm
from django.contrib.auth.decorators import login_required, permission_required

def listar_usuario_obras(request):
    registros = UsuarioObra.objects.all()
    return render(request, 'usuario_obra/lista_usuario_obras.html', {'registros': registros})


@login_required(login_url='login')
@permission_required('usuario_obra.add_usuarioobra', login_url='login', raise_exception=True)

def criar_usuario_obra(request):
    if request.method == 'POST':
        form = UsuarioObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuario_obras')
    else:
        form = UsuarioObraForm()
    return render(request, 'usuario_obra/form_usuario_obra.html', {'form': form})