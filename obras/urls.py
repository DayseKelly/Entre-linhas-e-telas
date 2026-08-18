from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_obras, name='listar_obras'),
    path('criar/', views.criar_obra, name='criar_obra'),
]