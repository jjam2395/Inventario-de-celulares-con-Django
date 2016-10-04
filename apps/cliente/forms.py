from django import forms
from apps.venta.models import cliente

class clienteform(forms.ModelForm):
	class Meta:
		model= cliente
		fields=['id_cliente','nombre','paterno','materno','direccion','telefono','f_nacer']
		labels={'id_cliente':'ID de cliente','nombre':'Nombre','paterno':'A. Paterno','materno':'A. Materno','direccion':'Direccion','telefono':'Telefono','fnacer':'Fecha de nacimiento'}

		widget={
		'id_cliente':forms.TextInput(attrs={'class':'form-control'}),
		'nombre':forms.Select(attrs={'class':'form-control'}),
		'paterno':forms.Select(attrs={'class':'form-control'}),
		'materno':forms.TextInput(attrs={'class':'form-control'}),
		'direccion':forms.TextInput(attrs={'class':'form-control'}),
		'telefono':forms.TextInput(attrs={'class':'form-control'}),
		'f_nacer':forms.TextInput(attrs={'class':'form-control'}),
		}



