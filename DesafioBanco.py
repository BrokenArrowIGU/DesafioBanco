#!/usr/local/bin/python
# coding: latin-1
import os, sys
# Definices Globais
saldo = 0
limite_s = 500
n_saque = 0
limite_diario = 3

# Programa geral
while True:
    print( f""" 
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair
    """ )
    opt = input("Escolha uma opção: ")
    
    # Deposito
    if opt == "d":
        saldo_p = float(input("Qual o valor do seu depósito? "))
        if saldo_p <= 0:
            print("Valor inv?lido, somente valores positivos, tente novamente.")
        else:
            saldo += saldo_p
            print(f"Deposito de R${saldo_p:.2f} realizado com sucesso.")
    
    # Saque
    elif opt == "s":
        if saldo == 0:
            print("Sem valor disponível para saque!")
        elif n_saque >= limite_diario:
            print("Limite diario de saques atingido, tente em data posterior.")
        else:
            saque = float(input("Qual o valor do saque? "))
            if saque > limite_s:
                print("Saque não permitido, valor acima do limite.")
            elif saque > saldo:
                print("Saque não permitido, saldo insuficiente.")
            else:
                saldo -= saque
                n_saque += 1
                print(f"Saque de R${saque:.2f} realizado com sucesso.")
    
    # Extrato
    elif opt == "e":
        print(f"""
Extrato:
Saques Diários: {n_saque}
Saques Ainda Permitidos: {limite_diario - n_saque}
Saldo Disponível: R${saldo:.2f}
""")
    
    # Sair
    elif opt == "q":
        break
    
    else:
        print("Operação inválida\nSelecione novamente a operação desejada.")
quit