from django.shortcuts import render, redirect
from app.forms2 import ProdutosForm, EmpresasForm
from app.models import Empresas, Produtos

# Create your views here.

def home(request):
    data = {}
    data['db'] = Empresas.objects.all()
    return render(request, 'index.html', data)

def home_produtos(request, id_empresa):
    data = {}
    data['db'] = Produtos.objects.filter(empresa = id_empresa)
    return render(request, 'home_produtos.html', data)

def forms_produtos(request):
    data = {}
    data['forms_produtos'] = ProdutosForm()
    return render(request, 'forms_produtos.html', data)

def forms_empresas(request):
    data = {}
    data['forms_empresas'] = EmpresasForm()
    return render(request, 'forms_empresas.html', data)

def create_produtos(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_produtos.html')

def create_empresas(request):
    form_empresas = EmpresasForm(request.POST or None)
    if form_empresas.is_valid():
        form_empresas.save()
        return redirect('home')

def view_produtos(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    return render(request, 'view_produtos.html', data)

def view_empresas(request, pk):
    data = {}
    data['db'] = Empresas.objects.get(pk=pk)
    return render(request, 'view_empresas.html', data)

def edit_produtos(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['forms_produtos'] = ProdutosForm(instance=data['db'])
    return render(request, 'forms_produtos.html', data)

def edit_empresas(request, pk):
    data = {}
    data['db'] = Empresas.objects.get(pk=pk)
    data['forms_empresas'] = EmpresasForm(instance=data['db'])
    return render(request, 'forms_empresas.html', data)


def update_empresas(request, pk):
    data = {}
    data['db'] = Empresas.objects.get( pk=pk )
    form = EmpresasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def update_produtos(request, pk):
    data = {}
    data['db'] = Produtos.objects.get( pk=pk )
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home_produtos.html')

def delete_empresas(request, pk):
    db = Empresas.objects.get(pk=pk)
    db.delete()
    return  redirect('home')

def delete_produtos(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return  redirect('home_produtos.html')

