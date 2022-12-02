from django.http import HttpResponse
from django.template import loader


def probando_html(request):
    
    nom="Lucas"
    ap="Diorio"

    diccionario={"nombre":nom,"apellido":ap,"edad":28,"lista":[4,8,9,7,10,2,6]}
    
    plantilla=loader.get_template('template1.htmal')
    documento=plantilla.render(diccionario)

    return HttpResponse(documento)

def inicio(request):
    return HttpResponse("Pagina de Inicio")

def productos(request):
    return HttpResponse("Pagina de Productos")

def entradas(request):
    return HttpResponse("Pagina de Entradas")

def salidas(request):
    return HttpResponse("Pagina de Salidas")