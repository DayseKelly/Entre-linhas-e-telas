from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listar_usuario_obras, name='listar_usuario_obras'),
    path('criar/', views.criar_usuario_obra, name='criar_usuario_obra'),
    path('<int:id>/', views.detalhe_usuario_obra, name='detalhe_usuario_obra'),
    path('<int:id>/editar/', views.editar_usuario_obra, name='editar_usuario_obra'),
    path('<int:id>/excluir/', views.excluir_usuario_obra, name='excluir_usuario_obra'),
]