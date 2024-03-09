from django.shortcuts import render
from .forms import PainelSolarForm, InversorForm, UsinaForm

# Create your views here.
def cadastro_painelsolar(request):
    if request.method == 'POST':
        form = PainelSolarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma-url-para-redirecionar')
    else:
        form = PainelSolarForm()
    return render(request, 'usinas/cadastro_painelsolar.html', {'form': form})

def cadastro_inversor(request):
    if request.method == 'POST':
        form = InversorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url-para-a-pagina-de-sucesso')  # Substitua pela URL desejada
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
    
    return render(request, 'usinas/usinas.html')