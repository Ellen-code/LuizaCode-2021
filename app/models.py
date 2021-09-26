from django.db import models

# Create your models here.

class Empresas(models.Model):
    id = models.IntegerField(primary_key= True)
    url = models.CharField(max_length=255, default=" ")
    cnpj = models.CharField(max_length=14, default="14 dígitos")
    razaoSocial = models.CharField(max_length=10, default=" ")
    email = models.CharField(max_length=50, default=" ")
    cidade = models.CharField(max_length=20, default=" ")
    estado = models.CharField(max_length=2, default="Ex: SP" )

    def __str__(self):
        return self.razaoSocial + " - " + self.cnpj
    
class Produtos(models.Model):
    id = models.IntegerField(primary_key= True)
    url = models.CharField(max_length=255, default=" ")
    codigo = models.CharField(max_length=15, default=" ")
    produto = models.CharField(max_length=100, default=" ")
    marca = models.CharField(max_length=20, default=" ")
    quantidade = models.IntegerField()
    empresa = models.ForeignKey(Empresas, on_delete = models.CASCADE, default=" ")
    