from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import OrcamentoForm
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
