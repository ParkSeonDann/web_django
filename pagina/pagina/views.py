from django.shortcuts import render


def mostrar_principal(request):
    return render(request, 'index.html')
    
def mostrar_contactanos(request):
    return render(request, 'contacto.html')