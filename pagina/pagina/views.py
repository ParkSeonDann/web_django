from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .albumes import albumes
from .forms import *
from sweetify import success, warning, info, error

def mostrar_principal(request):
    return render(request, 'albumes.html')
    
def mostrar_contactanos(request):
    if request.method == "GET":
        contexto = {
            'formulario':MiPrimerFormulario()
        }
        return render(request, 'contacto.html', contexto)
    if request.method == "POST":
        formulario_usuario = MiPrimerFormulario(request.POST)
        es_valido = formulario_usuario.is_valid()
        if es_valido:
            contexto = {
                "mensaje":"Formulario Valido uwu"
            }
            return render(request, 'contacto.html', contexto)
        contexto = {
            "formulario":formulario_usuario
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

def mostrar_entrar(request):
    if request.method == 'GET':
        contexto = {
            'titulo': 'Bienvenido',
            'formulario':FormularioEntrar()
        }
        return render(request,'entrar.html',contexto)
    if request.method == 'POST':
        datos_usuario = FormularioEntrar(data=request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            username = datos_usuario.cleaned_data['usuario']
            password = datos_usuario.cleaned_data['contrasenia_usuario']
            usuario = authenticate(username=username,password=password)
            if usuario is not None:
                login(request, usuario)
                success(request, f'Bienvenido {usuario.username}')
                return redirect('pagina_albumes')
        contexto = {
            'titulo': 'Bienvenido',
            'formulario': datos_usuario
        }
        warning(request,'Usuario y contraseña incorrectos')
        return render(request,'entrar.html',contexto)

def mostrar_registro(request):
    # Usamos el nuevo formulario para mostrar los elementos con clases
    if request.method == 'GET':
        contexto = {
            'formulario': FormularioRegistro()
        }
        return render(request, 'registro.html', contexto)
    elif request.method == 'POST':
        formulario_usuario = FormularioRegistro(request.POST)
        es_valido = formulario_usuario.is_valid() # True Valido, False Invalido 
        if es_valido:
            formulario_usuario.save()
            success(request,'Bienvenido, gracias por registrarte')
            return redirect('mostrar_entrar')
        contexto = {
            'formulario': formulario_usuario
        }
        warning(request, 'Ups... complete los campos correctamente')
        return render(request, 'registro.html', contexto)

def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        success(request,'Nos vemos pronto!')
    return redirect('pagina_albumes')