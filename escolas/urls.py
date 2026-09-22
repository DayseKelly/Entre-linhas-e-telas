from django.urls import path
from . import views

urlpatterns = [
    path ('', views.listar_escolas, name='listar_escolas'),
    path ('nova/', views.criar_escola, name='criar_escola'),
]