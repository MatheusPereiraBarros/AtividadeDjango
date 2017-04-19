from django.db import models

#class Contato(models.Model):
#	nome = models.CharField(max_length=50)
#	endereco = models.CharField(max_length=200)
#	email = models.EmailField(max_length=100)
#	data_nascimento = models.DateField()
#	telefone = models.CharField(max_length=20)

#	def __str__(self):
#		return self.nome

# Create your models here.

class Cliente(models.Model):
	CPF = models.CharField(max_length=14)
	nome = models.CharField(max_length=30)
	endereco = models.CharField(max_length=35)
	complemento = models.CharField(max_length=50)
	cidade = models.CharField(max_length=25)
	estado = models.CharField(max_length=2)
	CEP = models.CharField(max_length=8)
	foneResidencial = models.CharField(max_length=15)
	foneTrabalho = models.CharField(max_length=15)
	rendaFamiliar = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.nome



class Produto(models.Model):
	codigoProduto = models.IntegerField()
	nomeProduto = models.CharField(max_length=35)
	quantidade = models.IntegerField()
	minQuantidade = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.codigoProduto


class Venda(models.Model):
	codigoVenda = models.AutoField(primary_key=True)
	codigoCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	dataVenda = models.DateField()
	valorTotal = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.codigoCliente

class Fornecedor(models.Model):
	CNPJ = models.CharField(max_length=20)
	nome = models.CharField(max_length=30)
	endereco = models.CharField(max_length=35)
	complemento = models.CharField(max_length=50)
	cidade = models.CharField(max_length=25)
	estado = models.CharField(max_length=2)
	CEP = models.CharField(max_length=8)
	fone = models.CharField(max_length=15)
	responsavel = models.CharField(max_length=30)
	website = models.CharField(max_length=80)

	def __str__(self):
		return self.nome


class Pedido(models.Model):
	codigo = models.AutoField(primary_key=True)
	dataPedido = models.DateField()
	dataRecebimento = models.DateField()
	precoTotal = models.DecimalField(max_digits=10, decimal_places=2)
	codigoFornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

	def __str__(self):
		return self.codigo


class ItemVenda(models.Model):
	codigoVenda = models.ForeignKey(Venda, on_delete=models.CASCADE)
	#codigoProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
	codigoProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
	precoUnitario = models.DecimalField(max_digits=10, decimal_places=2)
	quantidade = models.IntegerField()

	def __str__(self):
		return self.codigoVenda


class ItemPedido(object):
	codigoPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
	codigoProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
	precoUnitario = models.DecimalField(max_digits=10, decimal_places=2)
	quantidade = models.IntegerField()

	def __str__(self):
		return self.codigoPedido

