from django.shortcuts import render, redirect
from .forms import OrcamentoForm


def criar_orcamento(request):
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Substitua 'index' pelo nome da URL para a qual você deseja redirecionar após o sucesso.
    else:
        form = OrcamentoForm()

    return render(request, 'contratos/criar_orcamento.html', {'form': form})
