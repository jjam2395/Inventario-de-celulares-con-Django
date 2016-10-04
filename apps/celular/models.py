from django.db import models

# Create your models here.
class celular(models.Model):
    id_celular=models.CharField(max_length=10,primary_key=True)
    nombre=models.CharField(max_length=30)
    fabricante=models.CharField(max_length=30)
    stock = models.IntegerField(blank=True, null=True)
    precio_compra=models.FloatField()
    precio_venta=models.FloatField()

    def __str__(self):
        return self.nombre
