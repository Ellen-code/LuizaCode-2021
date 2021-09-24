from django.shortcuts import render, redirect
from app.forms2 import ProdutosForm, EmpresasForm
from app.models import Empresas, Produtos

# Create your views here.

def home(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'index.html', data)

def cadastro_produtos(request):
    data = {}
    data['cadastro_produtos'] = ProdutosForm()
    return render(request, 'cadastro_produtos.html', data)

def cadastro_empresas(request):
    data = {}
    data['cadastro_empresas'] = EmpresasForm()
    return render(request, 'cadastro_empresas.html', data)

def create(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def create_empresas(request):
    form_empresas = EmpresasForm(request.POST or None)
    if form_empresas.is_valid():
        form_empresas.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def view_empresas(request, pk):
    data = {}
    data['db'] = Empresas.objects.get(pk=pk)
    return render(request, 'view_empresas.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['cadastro_produtos'] = ProdutosForm(instance=data['db'])
    return render(request, 'cadastro_produtos.html', data)

def update(request, pk):
    data = {}
    data['db'] = Produtos.objects.get( pk=pk )
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return  redirect('home')