from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('obras/', include('obras.urls')),
    path('escolas/', include('escolas.urls')),
    path('avaliacoes/', include('avaliacoes.urls')),
    path('usuario-obra/', include('usuario_obra.urls')),
    path('usuarios/', include('usuarios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)