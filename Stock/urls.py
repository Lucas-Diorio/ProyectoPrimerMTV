from django.urls import path
from Stock.views import *

urlpatterns = [
    
    path('', inicio, name="inicio"),
    path('productos/', productos, name="productos"),
    path('entradas/', entradas, name="entradas"),
    path('salidas/', salidas, name="salidas"),
    path('productoFormulario/', productoFormulario, name="productoFormulario"),
    path('busquedaProducto/', busquedaProducto, name="busquedaProducto"),
    path('buscar/', buscar, name="buscar"),
]