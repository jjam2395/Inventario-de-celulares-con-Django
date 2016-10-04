from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import celular
from django.http import HttpResponse
from .forms import celularform
# Create your views here.

# class index(TemplateView):
#     template_name='celulares/index.html'
class buscar(TemplateView):
    def post(self,request, *args, **kwars):
        busca=request.POST['buscalo']
        cel=celular.objects.filter(nombre__contains=busca)
        return render(request,"celulares/buscar.html", {'celulares':cel})

class registrar(CreateView):#clase para registrar celulares
    model=celular
    form_class=celularform
    template_name="celulares/registrar.html"
    success_url=reverse_lazy('inventario:registro')

class index(ListView):#clase para listar todos los elementos
    model=celular
    template_name="celulares/index.html"

class modificar(UpdateView):#clase para modificar un elemento en un formulario
    model=celular
    form_class=celularform
    template_name="celulares/registrar.html"
    success_url=reverse_lazy('inventario:index')

class eliminar(DeleteView):#clase para eliminar un elemento
    model=celular
    template_name="celulares/eliminar.html"
    success_url=reverse_lazy('inventario:index')
