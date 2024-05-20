from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import OrcamentoForm
from .models import Orcamento
from clientes.models import Cliente
from clientes.models import Propriedade
from django.http import JsonResponse

def cadastrar_orcamento(request, cliente_id=None):
    cliente = get_object_or_404(Cliente, pk=cliente_id) if cliente_id else None

    if request.method == 'POST':
        form = OrcamentoForm(request.POST, cliente_id=cliente_id)
        print("Dados do formulário submetido:", request.POST)  # Print dos dados submetidos
        if form.is_valid():
            novo_orcamento = form.save(commit=False)
            novo_orcamento.cliente = cliente  # Define o cliente diretamente com o objeto recuperado
            novo_orcamento.save()
            # Não esqueça de salvar as instâncias ManyToMany, se seu modelo Orcamento as tiver
            form.save_m2m()  
            return redirect(reverse('detalhar_cliente', args=[cliente_id]))
    else:
        # Pré-seleciona o cliente no formulário usando 'initial' e ajusta o queryset de propriedades
        form = OrcamentoForm(initial={'cliente': cliente}, cliente_id=cliente_id if cliente else None)

    context = {
        'form': form,
        'cliente_id': cliente_id
    }
    return render(request, 'contratos/cadastrar_orcamento.html', context)


def detalhar_orcamento(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    if request.method == 'POST':
        form = OrcamentoForm(request.POST, instance=orcamento)
        print("Dados do formulário submetido:", request.POST)  # Print dos dados submetidos
        if form.is_valid():
            print("Formulário válido e salvo.")  # Confirmação de formulário válido
            form.save()
            # Redirecione para a view de detalhes do orçamento, por exemplo
            return redirect(reverse('detalhar_cliente', args=[orcamento.cliente.id]))
        else:
            print("Erros no formulário:", form.errors)  # Print dos erros no formulário
    else:
        form = OrcamentoForm(instance=orcamento)
        cliente_id = orcamento.cliente.id
    #cliente_id = orcamento.cliente.id

    propriedades = Propriedade.objects.filter(cliente=orcamento.cliente)
    print("Propriedades disponíveis:", propriedades)  # Print das propriedades disponíveis

    return render(request, 'contratos/detalhar_orcamento.html', {'form': form, 'orcamento_id': orcamento_id, 'cliente_id':cliente_id})


def orcamentos(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'contratos/orcamentos.html', {'orcamentos': orcamentos})

def propriedades_por_cliente(request, cliente_id):
    propriedades = Propriedade.objects.filter(cliente_id=cliente_id)
    propriedades_data = [
        {
            'id': propriedade.id,
            'descricao': f"{propriedade.nome} - {propriedade.get_propriedade_display()} ({propriedade.cliente.nome_completo})"
        }
        for propriedade in propriedades
    ]
    return JsonResponse(propriedades_data, safe=False)