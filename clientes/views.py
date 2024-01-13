from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
# Create your views here.
def clientes(request):
        clientes = Cliente.objects.all()
        return render(request, 'clientes/clientes.html',{'clientes': clientes})
