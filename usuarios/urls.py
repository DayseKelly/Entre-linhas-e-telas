from django.urls import path
from . import views

urlpatterns = [
    path ('', views.listar_usuarios, name='listar_usuarios'),
    path ('novo/', views.criar_usuario, name='criar_usuario'),  
    path('login/', views.fazer_login, name='login'),
    path('logout/', views.fazer_logout, name='logout'),

]