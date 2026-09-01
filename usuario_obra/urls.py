from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listar_usuario_obras, name='listar_usuario_obras'),
    path('criar/', views.criar_usuario_obra, name='criar_usuario_obra'),
]