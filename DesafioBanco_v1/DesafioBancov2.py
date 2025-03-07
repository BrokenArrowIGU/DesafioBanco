
#!/usr/local/bin/python
# coding: latin-1
import os, sys

# Definições Globais
saldo = 0
agencia = "0001"
limite_s = 500
n_saque = 0
limite_diario = 3
contas = []
users = []
extrato = ""

# Funções

def deposito(saldo,valor,extrato,/):
   
    if valor <= 0:
            print("Valor inválido, somente valores positivos, tente novamente.")
    else:
            saldo += valor
            extrato+= f"Deposito de R${valor:.2f}\n"
            print("Deposito realizado com sucesso.")
    return saldo, extrato
    
def listextrato(saldo,extrato):
    print("\n \====== Extrato ======\\n")
    print("Não existem movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR${saldo:.2f}")	
	
def f_users(cpf,user):
    users_f = [usuario for usuario in user if usuario["cpf"] == cpf]
    return users_f[0] if users_f else None

def newuser(users):
    cpf = input("Informe o CPF (somente número): ")
    user = f_users(cpf,users)

    if user:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, n - bairro - cidade/sigla estado): ")

    users.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")
    return None

def saque(*,saldo,valor,extrato,limite_s,n_saque,limite_diario):
    if saldo == 0:
            print("Sem valor disponível para saque!")
    elif n_saque >= limite_diario:
            print("Limite diario de saques atingido, tente em data posterior.")
    else:
            if valor > limite_s:
                print("Saque não permitido, valor acima do limite.")
            elif valor > saldo:
                print("Saque não permitido, saldo insuficiente.")
            else:
                saldo -= valor
                n_saque += 1
                extrato += f"Saque de R${valor:.2f}\n"
                print("\nSaque realizado com sucesso!")
    return saldo, extrato

def novaconta(agencia,n_contas,users):
    cpf = input("Informe o CPF do usuário: ")
    usuario = f_users(cpf,users)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": n_contas, "usuario": usuario}

    print("\n Usuário não encontrado!")

def listusers(contas):
    print("\nLista de Usuários:")
    for conta in contas:
        ex = f"""\
          Agência: {conta['agencia']}
          Conta: {conta['numero_conta']}
          Titular: {conta['usuario']['nome']}
        """
    print(ex)

# Programa geral
while True:
    print( f""" 
    [d] Depósito
    [s] Saque
    [e] Extrato
    [nu] Novo Usuário
    [l] Lista de Usuários
    [nc] Nova Conta
    [q] Sair
    """ )
    opt = input("Escolha uma opção: ")
    
    # Deposito
    if opt == "d":
        valor = float(input("Qual o valor do seu depósito? "))
        saldo,extrato = deposito(saldo,valor,extrato)
        
    # Saque
    elif opt == "s":
         valor = float(input("Qual o valor do seu saque? "))
         saldo,extrato = saque(saldo=saldo,valor=valor,extrato=extrato,limite_s=limite_s,n_saque=n_saque,limite_diario=limite_diario)
    
    # Extrato
    elif opt == "e":
        listextrato(saldo,extrato)

    # Novo Usuário
    elif opt == "nu":
        newuser(users)

    # Lista de Usuários
    elif opt == "l":
        listusers(contas)

    # Nova Conta
    elif opt == "nc":
        n_contas = len(contas)+1 
        conta = novaconta(agencia,n_contas,users)

        if conta:
            contas.append(conta)  
            
            
# Sair
    elif opt == "q":
        break
    
    else:
        print("Operação inválida\nSelecione novamente a operação desejada.")
quit