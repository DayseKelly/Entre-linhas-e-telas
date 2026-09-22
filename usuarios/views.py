from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.forms import AuthenticationForm       
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required("usuario.view_usuario")
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


@login_required
@permission_required("usuario.add_usuario")
def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form': form})

def fazer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redireciona para a página principal (ex: lista de obras)
            return redirect('listar_obras')
    else:
        form = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def fazer_logout(request):
    logout(request)
    return redirect('login')


