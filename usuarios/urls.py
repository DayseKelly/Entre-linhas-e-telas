from django.urls import path
from . import views

urlpatterns = [
    path ('', views.listar_usuarios, name='listar_usuarios'),
    path ('novo/', views.criar_usuario, name='criar_usuario'),  
    path('<int:id>/', views.detalhe_usuario, name='detalhe_usuario'),
    path('<int:id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('<int:id>/excluir/', views.excluir_usuario, name='excluir_usuario'),
    path('login/', views.fazer_login, name='login'),
    path('logout/', views.fazer_logout, name='logout'),

]