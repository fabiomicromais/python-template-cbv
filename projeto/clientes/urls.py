# clientes/urls.py
from django.urls import path
from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView
)

urlpatterns = [
    path('', ClienteListView.as_view(), name='lista_clientes'),
    path('novo/', ClienteCreateView.as_view(), name='criar_cliente'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='editar_cliente'),
    path('deletar/<int:pk>/', ClienteDeleteView.as_view(), name='deletar_cliente'),
]
        