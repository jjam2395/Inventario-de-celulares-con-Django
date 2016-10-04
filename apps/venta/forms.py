from django import forms
from apps.venta.models import venta

class ventaform(forms.ModelForm):

    class Meta:
        model= venta

        fields=['id_venta','id_cliente','id_celular','cantidad','total']

        labels={'id_venta':'ID de venta','id_cliente':'Cliente','id_celular':'Modelo de celular','cantidad':'Cantidad','total':'Total'}

        widget={
        'id_venta':forms.TextInput(attrs={'class':'form-control'}),
        'id_cliente':forms.Select(attrs={'class':'form-control'}),
        'id_celular':forms.Select(attrs={'class':'form-control'}),
        'cantidad':forms.TextInput(attrs={'class':'form-control'}),
        'total':forms.TextInput(attrs={'class':'form-control'}),
        }
