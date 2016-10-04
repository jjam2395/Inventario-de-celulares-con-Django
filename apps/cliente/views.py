from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import cliente
from django.http import HttpResponse
from .forms import clienteform
# Create your views here


# class index(TemplateView):
#     template_name='clientes/index.html'
class buscar(TemplateView):
    def post(self,request, *args, **kwars):
        busca=request.POST['buscalo']
        client=cliente.objects.filter(nombre__contains=busca)
        return render(request,"clientes/buscar.html", {'clientes':client})

class registrar(CreateView):#clase para registrar clientes
    model=cliente
    form_class=clienteform
    template_name="clientes/registrar.html"
    success_url=reverse_lazy('cliente:registro')

class index(ListView):#clase para listar todos los elementos
    model=cliente
    template_name="clientes/index.html"

class modificar(UpdateView):#clase para modificar un elemento en un formulario
    model=cliente
    form_class=clienteform
    template_name="clientes/registrar.html"
    success_url=reverse_lazy('cliente:index')

class eliminar(DeleteView):#clase para eliminar un elemento
    model=cliente
    template_name="clientes/eliminar.html"
    success_url=reverse_lazy('cliente:index')
