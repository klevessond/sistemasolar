from django.shortcuts import render, redirect, get_object_or_404
from .forms import PainelSolarForm, InversorForm, UsinaForm
from . models import PainelSolar, Inversor

# Create your views here.
def cadastro_painelsolar(request):
    if request.method == 'POST':
        form = PainelSolarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usinas')
    else:
        form = PainelSolarForm()
    return render(request, 'usinas/cadastro_painelsolar.html', {'form': form})

def cadastro_inversor(request):
    if request.method == 'POST':
        form = InversorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usinas')  # Substitua pela URL desejada
    else:
        form = InversorForm()
    return render(request, 'usinas/cadastro_inversor.html', {'form': form})

def cadastro_usina(request):
    if request.method == 'POST':
        form = UsinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url-para-a-pagina-de-sucesso')  # Substitua pela URL desejada
    else:
        form = UsinaForm()
    return render(request, 'usinas/cadastro_usina.html', {'form': form})

def usinas(request):
    painelsolar = PainelSolar.objects.all()
    inversor = Inversor.objects.all()
    painelform = PainelSolarForm()
    inversorform = InversorForm()
    
    
    return render(request, 'usinas/usinas.html',{'painelsolar':painelsolar,'inversor':inversor,
                                                 'painelform':painelform,'inversorform':inversorform})

def editar_painelsolar(request, painelsolar_id):
    painelsolar = get_object_or_404(PainelSolar, id=painelsolar_id)
    if request.method == 'POST':
        form = PainelSolarForm(request.POST, instance=painelsolar)
        if form.is_valid():
            form.save()
            return redirect('detalhar_painelsolar', painelsolar_id)  # Redireciona para a página de clientes após a edição
    else:
        form = PainelSolarForm(instance=painelsolar)
    return render(request, 'usinas/editar_painelsolar.html', {'form': form, 'painelsolar': painelsolar})

def editar_inversor(request, inversor_id):
    inversor = get_object_or_404(Inversor, id=inversor_id)
    if request.method == 'POST':
        form = PainelSolarForm(request.POST, instance=inversor)
        if form.is_valid():
            form.save()
            return redirect('detalhar_inversor', inversor_id)  # Redireciona para a página de clientes após a edição
    else:
        form = PainelSolarForm(instance=painelsolar)
    return render(request, 'usinas/editar_inversor.html', {'form': form, 'inversor': inversor})