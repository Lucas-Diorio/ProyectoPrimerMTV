from django import forms

class ProductoForm(forms.Form):
    nroparte=forms.IntegerField()
    nombre=forms.CharField(max_length=50)
    costo=forms.FloatField()
    cantidad=forms.IntegerField()

class EntradasForm(forms.Form):
    nroentrada=forms.IntegerField()
    fecha=forms.DateField()
    descripcion=forms.CharField(max_length=50)
    cantidad=forms.IntegerField()
    costo=forms.FloatField()

class SalidasForm(forms.Form):
    nrosalida=forms.IntegerField()
    fecha=forms.DateField()
    descripcion=forms.CharField(max_length=50)
    cantidad=forms.IntegerField()
    costo=forms.FloatField()