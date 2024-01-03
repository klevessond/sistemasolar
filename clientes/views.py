from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def clientes(request):
        return HttpResponse('<h1>tela de clientes</h1>')
