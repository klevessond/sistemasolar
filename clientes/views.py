from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Cliente, Estado, Cidade, Bairro
from .forms import ClienteForm, EstadoForm, CidadeForm, BairroForm, PropriedadeForm
from django.urls import reverse
from django.db.models import Max

def cadastro_estado(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        print(form)
        if form.is_valid():
            # Verifique se a origem é da página cadastro_cliente
            print('Dados recebidos no POST:', request.POST)
            origin_page = request.POST.get('origin_page')
            print('origem:', origin_page)
            if origin_page == 'cadastro_cliente':
                # Salvar o estado no banco de dados
                form.save()
                max_id_estado = Estado.objects.all().aggregate(Max('id'))['id__max']  # Obtém o maior ID dos estados
                return redirect(reverse('cadastro_cliente') + f'?max_id_estado={max_id_estado}')


            else:
                    return redirect('lista_estado')
    else:
        # Se o request não for POST, crie um formulário vazio
        form = EstadoForm()

    return render(request, 'clientes/cadastro_estado.html', {'form': form})

def cadastro_cidade(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            # Verifique se a origem é da página cadastro_cliente
            print('Dados recebidos no POST:', request.POST)
            origin_page = request.POST.get('origin_page')
            print('origem:', origin_page)
            if origin_page == 'cadastro_cliente':
                # Salvar o estado no banco de dados
                form.save()
                max_id_cidade = Cidade.objects.all().aggregate(Max('id'))['id__max']  # Obtém o maior ID dos estados
                return redirect(reverse('cadastro_cliente') + f'?max_id_cidade={max_id_cidade}')
            else:
                return redirect('lista_cidade')
    else:
        form = CidadeForm()

    return render(request, 'clientes/cadastro_cidade.html', {'form': form})

def cadastro_bairro(request):
    if request.method == 'POST':
        form = BairroForm(request.POST)
        if form.is_valid():
            # Verifique se a origem é da página cadastro_cliente
            print('Dados recebidos no POST:', request.POST)
            origin_page = request.POST.get('origin_page')
            print('origem:', origin_page)
            if origin_page == 'cadastro_cliente':
                # Salvar o estado no banco de dados
                form.save()
                max_id_bairro = Bairro.objects.all().aggregate(Max('id'))['id__max']  # Obtém o maior ID dos estados
                return redirect(reverse('cadastro_cliente') + f'?max_id_bairro={max_id_bairro}')
            else:
                return redirect('lista_bairro')
    else:
        form = BairroForm()

    return render(request, 'clientes/cadastro_bairro.html', {'form': form})

# Create your views here.
def clientes(request):
    limpar_store = request.GET.get('limpar_store')  # Captura o parâmetro limpar_store da URL
    if limpar_store:
        # Lógica para limpar a store local, se necessário
        # Aqui você pode fazer o que for necessário com o parâmetro limpar_store
        print('Limpar store:', limpar_store)
    clientes = Cliente.objects.select_related('cidade', 'bairro', 'estado').all()
    print('limpar',limpar_store)
    return render(request, 'clientes/clientes.html', {'clientes': clientes, 'limpar_store': limpar_store})

def cadastro_cliente(request):
    max_id_estado = request.GET.get('max_id_estado')  # Captura o parâmetro
    max_id_cidade = request.GET.get('max_id_cidade')  # Captura o parâmetro
    max_id_bairro = request.GET.get('max_id_bairro')  # Captura o parâmetro
    if request.method == 'POST':
        form = ClienteForm(request.POST or None)
        print(form)
        print('Dados recebidos no POST:', request.POST)
        if form.is_valid():
            # Salve os dados do formulário no banco de dados
            form.save()
            return redirect(reverse('clientes') + '?limpar_store=1')

        else:
            # Se o formulário não for válido, imprima mensagens de erro específicas para cada campo
            for field, errors in form.errors.items():
                print(f'Erro no campo {field}: {", ".join(errors)}')
            return render(request, 'clientes/cadastro_cliente.html', {'form': form})

    else:
        cliente_form_data = request.session.get('cliente_form_data', {})
        form = ClienteForm()
        formEstados = EstadoForm()
        formCidade = CidadeForm()
        formBairro = BairroForm()
        #max_id = None
        return render(request, 'clientes/cadastro_cliente.html',
         {'cliente_form_data': cliente_form_data,'form': form,'formEstados':formEstados,'formCidade':formCidade,
          'formBairro':formBairro, 'max_id_estado':max_id_estado,'max_id_cidade':max_id_cidade, 'max_id_bairro':max_id_bairro })

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')  # Redireciona para a página de clientes após a edição
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})



def get_cidades(request):
    estado_id = request.GET.get('estado_id')
    cidades = Cidade.objects.filter(estado_id=estado_id).order_by('nome')  # Ordena por nome
    data = [{'id': cidade.id, 'nome': cidade.nome} for cidade in cidades]
    return JsonResponse(data, safe=False)

def get_bairros(request):
    cidade_id = request.GET.get('cidade_id')
    bairros = Bairro.objects.filter(cidade_id=cidade_id).order_by('nome')  # Ordena por nome
    data = [{'id': bairro.id, 'nome': bairro.nome} for bairro in bairros]
    return JsonResponse(data, safe=False)

def cadastro_propriedade(request):
    if request.method == 'POST':
        form = PropriedadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propriedades_listar')  # Supondo que você tenha uma URL para listar propriedades
    else:
        form = PropriedadeForm()
    return render(request, 'clientes/cadastro_propriedade.html', {'form': form})