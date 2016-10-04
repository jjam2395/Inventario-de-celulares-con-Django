from django.db import models

# Create your models here.
class cliente(models.Model):
    id_cliente = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=30)
    paterno = models.CharField(max_length=30)
    materno = models.CharField(max_length=30)
    direccion = models.CharField(blank=True, max_length=50)
    telefono = models.CharField(blank=True, max_length=10)
    f_nacer = models.DateField()

    def __str__(self):
            self.nomb=self.nombre + " " +self.paterno
            return self.nomb
