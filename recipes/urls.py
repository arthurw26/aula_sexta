"""
URL configuration for aula_sexta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse
from recipes.views import _home, _contato, _sobre 


# HTTP REQUEST <- RESPONSE
#def home(request):
#   return HttpResponse('home')

urlpatterns = [
    path('', _home),#home
    path('sobre/', _sobre),#sobre
    path('contato/', _contato),#contato
]
