from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def _home(request):
    return render(request, 'home.html')

def _sobre(request):
    return HttpResponse('sobre')

def _contato(request):
    return HttpResponse('contato')