from django.forms import ModelForm
from app.models import Empresas, Produtos

# Create the form class.

class EmpresasForm(ModelForm):
    class Meta:
        model = Empresas
        fields = ['url', 'cnpj', 'razaoSocial', 'email', 'cidade', 'estado']

        
class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['url', 'codigo', 'produto', 'marca', 'quantidade', 'empresa']

