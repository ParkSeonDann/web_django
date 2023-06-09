from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',mostrar_principal, name='pagina_principal'),
    path('contacto/',mostrar_contactanos, name='pagina_contactanos'),
    path('albumes/',mostrar_albumes, name='pagina_albumes'),
    path('precios/',mostrar_precios, name='pagina_precios'),
    path('entrar/',mostrar_entrar,name='mostrar_entrar'),
    path('registrar/',mostrar_registro, name='mostrar_registro'),
    path('salir/',cerrar_sesion, name='cerrar_sesion'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG == True: 
    urlpatterns += static(settings.STATIC_URL, root_document = settings.STATIC_ROOT)