# clientes/urls.py
from django.urls import path
from . import views
from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', ClienteListView.as_view(), name='lista_clientes'),
    path('novo/', ClienteCreateView.as_view(), name='criar_cliente'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='editar_cliente'),
    path('deletar/<int:pk>/', ClienteDeleteView.as_view(), name='deletar_cliente'),
]
        