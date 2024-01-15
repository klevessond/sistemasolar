from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm


# Create your views here.
def clientes(request):
        clientes = Cliente.objects.select_related('cidade', 'bairro', 'estado').all()
        return render(request, 'clientes/clientes.html',{'clientes': clientes})

def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Salve os dados do formulário no banco de dados
            form.save()
            return redirect('sucesso')  # Redirecione para a página de sucesso após o envio
    else:
        form = ClienteForm()


        return render(request, 'clientes/novo_cliente.html', {'form': form})
