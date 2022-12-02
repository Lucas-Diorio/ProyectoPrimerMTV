from django.db import models

# Create your models here.

class Productos(models.Model):

    nroparte=models.IntegerField()
    descripcion=models.CharField(max_length=50)
    costo=models.FloatField()
    cantidad=models.IntegerField()

    def __str__(self):
        return self.descripcion+" "+str(self.cantidad)


class Entradas(models.Model):

    nroentrada=models.IntegerField()
    fecha=models.DateField()
    descripcion=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    costo=models.FloatField()

    def __str__(self):
        return self.descripcion+" "+str(self.cantidad)


class Salidas(models.Model):

    nrosalida=models.IntegerField()
    fecha=models.DateField()
    descripcion=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    costo=models.FloatField()

    def __str__(self):
        return self.descripcion+" "+str(self.cantidad)