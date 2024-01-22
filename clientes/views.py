from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Cliente, Estado, Cidade, Bairro
from .forms import ClienteForm


# Create your views here.
def clientes(request):
        clientes = Cliente.objects.select_related('cidade', 'bairro', 'estado').all()
        return render(request, 'clientes/clientes.html',{'clientes': clientes})

def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST or None)
        if form.is_valid():
            # Salve os dados do formulário no banco de dados
            form.save()
            return redirect('sucesso')  # Redirecione para a página de sucesso após o envio
    else:
        form = ClienteForm()


        return render(request, 'clientes/novo_cliente.html', {'form': form})

def get_cidades(request):
    estado_id = request.GET.get('estado_id')
    cidades = Cidade.objects.filter(estado_id=estado_id)
    data = [{'id': cidade.id, 'nome': cidade.nome} for cidade in cidades]
    return JsonResponse(data, safe=False)

def get_bairros(request):
    cidade_id = request.GET.get('cidade_id')
    bairros = Bairro.objects.filter(cidade_id=cidade_id)
    data = [{'id': bairro.id, 'nome': bairro.nome} for bairro in bairros]
    return JsonResponse(data, safe=False)
