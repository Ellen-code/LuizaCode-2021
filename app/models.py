from django.db import models

# Create your models here.
# Create your models here.
class Produtos(models.Model):
    cnpj = models.CharField(max_length=14)
    codigo = models.CharField(max_length=10)
    produto = models.CharField(max_length=100)
    marca = models.CharField(max_length=20)
    quantidade = models.IntegerField()

class Empresas(models.Model):
    cnpj = models.CharField(max_length=14, default="14 dígitos")
    razaoSocial = models.CharField(max_length=10, default=" ")
    email = models.CharField(max_length=50, default=" ")
    cidade = models.CharField(max_length=20, default=" ")
    estado = models.CharField(max_length=2, default="Ex: SP" )
    