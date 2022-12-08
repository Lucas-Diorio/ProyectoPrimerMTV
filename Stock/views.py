from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from Stock.forms import ProductoForm,EntradasForm,SalidasForm
from .models import *



def inicio(request):
    return render(request, "Stock/inicio.html")

def productos(request):
    return render(request, "Stock/productos.html")

def entradas(request):
    return render(request, "Stock/entradas.html")

def salidas(request):
    return render(request, "Stock/salidas.html")

def productoFormulario(request):
    
    if request.method=="POST":
        form=ProductoForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            productito=informacion["descripcion"]
            cantidadd=informacion["cantidad"]
            nroorden=informacion["nroparte"]
            costito=informacion["costo"]

            producto1=Productos(nroparte=nroorden,descripcion=productito,costo=costito,cantidad=cantidadd)
            producto1.save()
            return render(request, "Stock/inicio.html")

    else:
        formulario=ProductoForm()

    return render(request, "Stock/productoFormulario.html", {"form":formulario})


def entradas(request):
    
    if request.method=="POST":
        form=EntradasForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nroentrada=informacion["nroentrada"]
            fecha=informacion["fecha"]
            descripcion=informacion["descripcion"]
            cantidad=informacion["cantidad"]
            costo=informacion["costo"]


            entrada1=Entradas(nroentrada=nroentrada,fecha=fecha,descripcion=descripcion,cantidad=cantidad,costo=costo)
            entrada1.save()
            return render(request, "Stock/inicio.html", {"mensaje":"ENTRADA INGRESADA CORRECTAMENTE!"})

    else:
        formulario=EntradasForm()

    return render(request, "Stock/entradas.html", {"form":formulario})
    
def salidas(request):
    
    if request.method=="POST":
        form=SalidasForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nroentrada=informacion["nroentrada"]
            fecha=informacion["fecha"]
            descripcion=informacion["descripcion"]
            cantidad=informacion["cantidad"]
            costo=informacion["costo"]


            salidas1=Salidas(nroentrada=nroentrada,fecha=fecha,descripcion=descripcion,cantidad=cantidad,costo=costo)
            salidas1.save()
            return render(request, "Stock/inicio.html", {"mensaje":"ENTRADA INGRESADA CORRECTAMENTE!"})

    else:
        formulario=EntradasForm()

    return render(request, "Stock/entradas.html", {"form":formulario})



    
def busquedaProducto(request):   
    return render(request, "Stock/busquedaProducto.html")

def buscar(request):

    if "nroparte" in request.GET:

        nroparte=request.GET["nroparte"]

        productos=Productos.objects.filter(nroparte=nroparte)
        return render(request, "Stock/resultadosBusqueda.html", {"productos":productos})
    else:
        return render(request, "Stock/busquedaProducto.html", {"mensaje":"Ingresa un producto"})