"""
URL configuration for pagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('admin/', admin.site.urls),
]

if settings.DEBUG == True: 
    urlpatterns += static(settings.STATIC_URL, root_document = settings.STATIC_ROOT)