from django.shortcuts import render
from .albumes import albumes
from .forms import *

def mostrar_principal(request):
    return render(request, 'index.html')
    
def mostrar_contactanos(request):
    contexto = {
        'formulario':MiPrimerFormulario()
    }
    return render(request, 'contacto.html', contexto)

def mostrar_albumes(request):
    resultado = albumes
    palabra = ""
    if request.method == 'GET':
        palabra_cliente = request.GET.get('busqueda')
        if palabra_cliente != None:
            palabra = palabra_cliente
            resultado = []
            for variable in albumes:
                if palabra_cliente.lower() in variable['nombre'].lower() or palabra_cliente.lower() in variable['fecha'].lower() or palabra_cliente.lower() in variable['autor'].lower() or palabra_cliente.lower() in variable['lugar'].lower() or palabra_cliente.lower() in variable['precio'].lower() or palabra_cliente.lower() in variable['caratula'].lower():
                    resultado.append(variable)
            
    context = {
        'titulo':'Albumes de musica',
        'lista': resultado,
        'palabra': palabra,
    }
    return render(request, 'albumes.html', context)

def mostrar_precios(request):
    context = {
        'titulo':'precios',
        'lista': albumes,
    }
    return render(request, 'precios.html', context)





