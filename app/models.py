from django.db import models

# Create your models here.
class Empresas(models.Model):
    #id = models.IntegerField(primary_key= True)
    cnpj = models.CharField(primary_key= True, max_length=14, default="14 dígitos")
    razaoSocial = models.CharField(max_length=10, default=" ")
    email = models.CharField(max_length=50, default=" ")
    cidade = models.CharField(max_length=20, default=" ")
    estado = models.CharField(max_length=2, default="Ex: SP" )

    
    def __str__(self):
        return self.razaoSocial
    


class Produtos(models.Model):
    #id = models.IntegerField(primary_key= True)
    cnpj = models.CharField(primary_key= True, max_length=14, default=" ")
    codigo = models.CharField(max_length=10, default=" ")
    produto = models.CharField(max_length=100, default=" ")
    marca = models.CharField(max_length=20, default=" ")
    quantidade = models.IntegerField()
    empresa = models.ForeignKey(Empresas, on_delete = models.CASCADE, default=" ")
    