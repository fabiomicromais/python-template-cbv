from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .forms import ClienteForm 
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views import View

from .models import Cliente


def index(request):
    template = loader.get_template('clientes/index.html')
    return HttpResponse(template.render({}, request))   


class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/lista.html'
    context_object_name = 'clientes'



class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('lista_clientes')



class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('lista_clientes')



class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/excluir.html'
    success_url = reverse_lazy('lista_clientes')

