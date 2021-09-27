from django.shortcuts import render, redirect
from app.forms2 import EmpresasForm, ProdutosForm
from app.models import Empresas, Produtos
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
  data ={}
  return render(request, 'index.html', data)

# empresas

def home(request):
  data = {}
  search = request.GET.get('search')
  if search:
    data['db'] = Empresas.objects.filter(razaoSocial__icontains = search)
  else:
    data['db'] = Empresas.objects.all()
  return render(request, 'home.html', data)

def forms_empresas(request):
  data = {'forms_empresas': EmpresasForm()}
  return render(request, 'forms_empresas.html', data)

def create_empresas(request):
    forms_empresas = EmpresasForm(request.POST or None)
    if forms_empresas.is_valid():
        forms_empresas.save()
        return HttpResponseRedirect('/home')

def view_empresas(request, pk):
    data = {'db': Empresas.objects.get(pk=pk)}
    return render(request, 'view_empresas.html', data)

def edit_empresas(request, pk):
    data = {}
    data['db'] = Empresas.objects.get(pk=pk)
    data['forms_empresas'] = EmpresasForm(instance=data['db'])
    return render(request, 'forms_empresas.html', data)

def update_empresas(request, pk):
    data = {}
    data['db'] = Empresas.objects.get( pk=pk )
    forms_empresas = EmpresasForm(request.POST or None, instance=data['db'])
    if forms_empresas.is_valid():
        forms_empresas.save()
        return HttpResponseRedirect('/home')

def delete_empresas(request, pk):
    db = Empresas.objects.get(pk=pk)
    db.delete()
    return HttpResponseRedirect('/home')

# produtos

def home_produtos(request):
  data = {}
  search = request.GET.get('search')
  if search:
    data['db'] = Produtos.objects.filter(razaoSocial__icontains = search)
  else:
    data['db'] = Produtos.objects.all()
  return render(request, 'home_produtos.html', data)

def forms_produtos(request):
    data = {'forms_produtos' : ProdutosForm}
    return render(request, 'forms_produtos.html', data)

def create_produtos(request):
    forms_produtos = ProdutosForm(request.POST or None)
    if forms_produtos.is_valid():
        forms_produtos.save()
        return HttpResponseRedirect('/home_produtos')

def view_produtos(request, pk):
    data = {'db': Produtos.objects.get(pk=pk)} 
    return render(request,'view_produtos.html', data)

def edit_produtos(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['forms_produtos'] = ProdutosForm(instance=data['db'])
    return render(request, 'forms_produtos.html', data)

def update_produtos(request, pk):
    data = {}
    data['db'] = Produtos.objects.get( pk=pk )
    forms_produtos = ProdutosForm(request.POST or None, instance=data['db'])
    if forms_produtos.is_valid():
        forms_produtos.save()
        return HttpResponseRedirect('/home_produtos')

def delete_produtos(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return HttpResponseRedirect('/home_produtos')

def produtos(request, pk):
   data = {'db': Produtos.objects.get(pk=pk)}
   return render(request, 'produtos.html', data)

