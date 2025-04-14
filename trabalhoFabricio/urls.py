"""
URL configuration for trabalhoFabricio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial_personalizada, name='pagina_inicial'),  # Mapeia a raiz para sua view
    path('apresentacao/', include('apresentacao.urls', namespace='apresentacao')),  # Adicionando o prefixo 'apresentacao/'
    path('blog/', include('blog.urls', namespace='blog')),            # Prefixo /blog/ para o blog
    path('galeria/', include('galeria.urls', namespace='galeria')),      # Prefixo /galeria/ para a galeria
]