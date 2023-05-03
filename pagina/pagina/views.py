from django.shortcuts import render
from .albumes import albumes

def mostrar_principal(request):
    return render(request, 'index.html')
    
def mostrar_contactanos(request):
    return render(request, 'contacto.html')

def mostrar_albumes(request):
    context = {
        'titulo':'Albumes de musica',
        'lista': albumes,
    }
    return render(request, 'albumes.html', context)

def mostrar_precios(request):
    context = {
        'titulo':'precios',
        'lista': albumes,
    }
    return render(request, 'precios.html', context)




