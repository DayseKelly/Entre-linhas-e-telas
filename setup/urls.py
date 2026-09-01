from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('obras/', include('obras.urls')),
    path('escolas/', include('escolas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('avaliacoes/', include('avaliacoes.urls')),
    path('usuario-obra/', include('usuario_obra.urls')),
]