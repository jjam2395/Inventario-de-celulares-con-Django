from django.shortcuts import render,redirect
from apps.venta.forms import ventaform
from django.http import HttpResponse
#from apps.venta.forms import ventaform
# Create your views here.
def index(request):
    return render(request,'ventas/index.html')

def registro_venta(request):
    if request.method== 'POST':
        form = ventaform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('venta:index')
    else:
        form=ventaform()

    return render(request, 'ventas/registrar_venta.html',{'form':form})
