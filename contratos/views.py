from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import OrcamentoForm
from .models import Orcamento
from clientes.models import Cliente

def criar_orcamento(request, cliente_id=None):
    cliente = get_object_or_404(Cliente, pk=cliente_id) if cliente_id else None

    if request.method == 'POST':
        form = OrcamentoForm(request.POST, cliente_id=cliente_id)
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
    return render(request, 'contratos/criar_orcamento.html', context)


def detalhar_orcamento(request, orcamento_id):
    orcamento = get_object_or_404(OrcamentoForm, id=orcamento_id)
    if request.method == 'POST':
        form = OrcamentoForm(request.POST, instance=orcamento)
        if form.is_valid():
            form.save()
            # Redirecione para a view de detalhes do orçamento, por exemplo
            return redirect(reverse('contratos/orcamentos.html'))
    else:
        form = OrcamentoForm(instance=orcamento)

    return render(request, 'contrato/detalhar_orcamento.html', {'form': form, 'orcamento_id': orcamento_id})


def orcamentos(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'contratos/orcamentos.html', {'orcamentos': orcamentos})
