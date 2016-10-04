from django.db import models
from apps.celular.models import celular
from apps.cliente.models import cliente
from django.utils import timezone
# Create your models here.
class venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(cliente,on_delete=models.CASCADE)
    id_celular = models.ForeignKey(celular,on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    cantidad = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
            return self.id_venta
