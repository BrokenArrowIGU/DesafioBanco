#!/usr/local/bin/python
# coding: latin-1
import os, sys
from abc  import ABC, abstractmethod, abstractproperty
from datetime import datetime

# Definições Globais
class cliente:
	def __init__(self, logradouro):
		self.logradouro = logradouro
		self.contas = []

	def realizatransacao(self,conta, transacao):
		transacao.registrar(conta)

	def addconta(self,conta):
		self.contas.append(conta)
class PF(cliente):
	def __init(self,nome,nascimento,cpf,logradouro):
		super().__init__(logradouro)
		self.nome = nome
		self.nascimento = nascimento
		self.cpf = cpf
class conta:
	def __init__(self,num,cliente):

		self._saldo = 0
		self._numero = num
		self._agencia = "0001"
		self._cliete = cliente
		self._history = history()

	@classmethod
	def newconta(cls,cliente,num):
		return cls(num,cliente)

	@property
	def saldo(self):
		return self._saldo

	@property
	def numero(self):
		return self._numero

	@property
	def agencia(self):
		return self._agencia

	@property
	def cliente(self):
		return self._cliente

	@property
	def historico(self):
		return self._historico

	def sacar(self,valor):
		saldo = self.saldo
		estourou = valor > saldo
		if estourou:
			print("Saque não permitido, saldo insuficiente.")
		elif valor > 0:
			saldo -= valor
			print("\nSaque realizado com sucesso!")
			return True
		else:
			print("\n Operação não permitida! Tente novamente.")
    	
		return False

	def deposito(self,valor):
		if valor <= 0:
			print("Valor inválido, somente valores positivos, tente novamente.")
		else:
			self.saldo += valor
		print("Deposito realizado com sucesso.")
class CC(cliente):
	def __init__(self, numero,cliente,limite=500, n_saque=3):
		super().__init__(numero,cliente)
		self.limite=limite
		self.nsaque=n_saque
	def sacar(self, valor):
		nsaque = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == saque.__name__])
		estourou_limite = valor > self.limite
		estourou_saque = nsaque >= self.nsaque
		if estourou_limite:
			print("\n Operação não permitida! Valor de saque inválido.")
		elif estourou_saque:
			print("\n Operação não permitida! Numero de saques excedido.")
		else:
			return super().sacar(valor)
		return False
	def __str__(self):
		return f"""\
		Agência:\t{self.agencia}
		C/c:\t\t{self.numero}
		Titular:\t{self.cliente.nome}
		"""
class history:
	def __init__(self):
		self._transacoes=[]
	@property
	def transacoes(self):
		return self._transacoes
	def addtransacao(self, transacao):
		self._transacoes.append(
			{
				"tipo": transacao._class_._name_,
				"valor":transacao.valor,
				"data":datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
			}
		)
class transacao(ABC):
	@property
	@abstractproperty
	def valor(self):
		pass
	@abstractproperty
	def registrar(self,conta):
		pass
class saque(transacao):
	def __init__(self, valor):
		self.valor = valor
	@property
	def valor(self):
		return self.valor
	def registrar(self,conta):
		certotransacao = conta.saque(self.valor)
		if certotransacao:
			conta.history.addtransacao(self)
class deposito(transacao):
	def __init__(self, valor):
		self.valor = valor
	@property
	def valor(self):
		return self.valor
	def registrar(self,conta):
		certotransacao = conta.deposito(self.valor)
		if certotransacao:
			conta.history.addtransacao(self)
def menu():
	menu = """\n\t====== MENU ======
	[d] Depósito
	[s] Saque
	[e] Extrato
	[nu] Novo Usuário
	[l] Lista de Usuários
	[nc] Nova Conta
	[q] Sair
	==================\n
	"""
	return menu

def listarclientes(cpf,clientes):
	clienteslistados = [cliente for cliente in clientes if cliente.cpf == cpf]
	return clienteslistados[0] if clienteslistados else None
def recuperarconta(contas):
	if not cliente.addconta:
		print("\n Cliente não encontrado.")
		return None
	return cliente.addconta[0]
def depositar(conta):
	cpf = input("\n Digite o CPF do cliente: ")
	cliente = listarclientes(cpf,cliente)
	if not cliente:
		print("\n Cliente não encontrado.")
		return
	valor = float(input("\n Digite o valor do depósito: "))
	operacao = deposito(valor)
	conta =	recuperarconta(cliente.contas)
	if not conta:
		print("\n Conta não encontrada.")
		return
	cliente.realizatransacao(conta,operacao)
def sacar(conta):
	cpf = input("\n Digite o CPF do cliente: ")
	cliente = listarclientes(cpf,cliente)
	if not cliente:
		print("\n Cliente não encontrado.")
		return
	valor = float(input("\n Digite o valor do saque: "))
	operacao = saque(valor)
	conta =	recuperarconta(cliente.contas)
	if not conta:
		print("\n Conta não encontrada.")
		return
	cliente.realizatransacao(conta,operacao)
def novousuario(clientes):
	
	cpf = input("\n Digite o CPF: ")
	cliente = listarclientes(cpf,clientes)
	if cliente:
		print("\n Cliente já cadastrado.")
		return
	nome = input("\n Digite o nome: ")
	nascimento = input("\n Digite a data de nascimento(dd-mm-yyyy): ")
	logradouro = input("\n Digite o endereço(rua, nro - bairro - cidade/UF ): ")
	cliente = PF(nome=nome,nascimento=nascimento,cpf=cpf,logradouro=logradouro)
	clientes.append(cliente)
	print("\n Cliente cadastrado com sucesso!")

def novaconta(numero,clientes,contas):
	cpf = input("\n Digite o CPF do cliente: ")
	cliente = listarclientes(cpf,clientes)
	if not cliente:
		print("\n Cliente não encontrado.")
		return
	conta = CC.newconta(cliente=cliente,numero=numero)
	contas.append(conta)
	cliente.contas.append(conta)
	print("\n Conta criada com sucesso!")

def listarclientes(contas):
	for conta in contas:
		print("#################")
		print(conta)
		
def extrato(clientes):
	cpf = input("\n Digite o CPF do cliente: ")
	cliente = listarclientes(cpf,clientes)
	if not cliente:
		print("\n Cliente não encontrado.")
		return
	conta = recuperarconta(cliente.contas)
	if not conta:
		return
	print("\n Extrato")
	operacao = conta.historico.transacoes
	ext = ""
	if not operacao:
		print("\n Não há operações realizadas.")
		return
	else:
		for operacao in operacao:
			ext += f"\n Tipo: {operacao['tipo']}"
			ext += f"\n Valor:\tR${operacao['valor']:.2f}"
			ext += f"\n Data: {operacao['data']}"
			ext += "\n"
	print(ext)
	print(f"\n Saldo: R${conta.saldo:.2f}")

def main():
	cliente = []
	contas = []

	while True:
		opcoes = menu()
		x = input(opcoes)

		if x == "d":
			depositar(conta)
		elif x == "s":
			sacar(conta)
		elif x == "e":
			extrato(conta)
		elif x == "nu":
			novousuario(cliente)
		elif x == "l":
			l = len(cliente)+1
			novaconta(l,cliente,contas)
		elif x == "nc":
			
			novaconta(cliente)
		elif x == "q":
			break
		else:
			print("\n Opção inválida! Tente novamente.")

main()