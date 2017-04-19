from django.contrib import admin
from .models import Cliente
from .models import Venda
from .models import ItemVenda
from .models import Produto
from .models import ItemPedido
from .models import Pedido
from .models import Fornecedor


class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome','endereco','foneResidencial')

class VendaAdmin(admin.ModelAdmin):
	list_display = ('codigoVenda','dataVenda','valorTotal','codigoCliente')

class ItemVendaAdmin(admin.ModelAdmin):
	list_display = ('codigoVenda','codigoProduto','precoUnitario','quantidade')

class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('codigoProduto','nomeProduto','quantidade','minQuantidade')


class PedidoAdmin(admin.ModelAdmin):
	list_display = ('codigo','dataPedido','dataRecebimento','precoTotal','codigoFornecedor')

class FornecedorAdmin(admin.ModelAdmin):
	list_display = ('CNPJ','nome','endereco','fone')



admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)


# Register your models here.class ClienteAdmin(admin.ModelAdmin):
	
