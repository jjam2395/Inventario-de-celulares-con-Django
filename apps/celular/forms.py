from django import forms
from apps.venta.models import celular

class celularform(forms.ModelForm):

    class Meta:
        model= celular

        fields=['id_celular','nombre','fabricante','stock','precio_compra','precio_venta']

        labels={'id_celular':'ID de celular','nombre':'Nombre','fabricante':'Fabricante','stock':'Stock','precio_compra':'Precio de compra','precio_venta':'Precio de venta'}

        widget={
        'id_celular':forms.TextInput(attrs={'class':'form-control'}),
        'nombre':forms.TextInput(attrs={'class':'form-control'}),
        'fabricante':forms.TextInput(attrs={'class':'form-control'}),
        'stock':forms.TextInput(attrs={'class':'form-control'}),
        'precio_compra':forms.TextInput(attrs={'class':'form-control'}),
        'precio_venta':forms.TextInput(attrs={'class':'form-control'}),
        }
