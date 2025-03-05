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
    [d] Dep�sito
    [s] Saque
    [e] Extrato
    [q] Sair
    """ )
    opt = input("Escolha uma op��o: ")
    
    # Deposito
    if opt == "d":
        saldo_p = float(input("Qual o valor do seu dep�sito? "))
        if saldo_p <= 0:
            print("Valor inv?lido, somente valores positivos, tente novamente.")
        else:
            saldo += saldo_p
            print(f"Deposito de R${saldo_p:.2f} realizado com sucesso.")
    
    # Saque
    elif opt == "s":
        if saldo == 0:
            print("Sem valor dispon�vel para saque!")
        elif n_saque >= limite_diario:
            print("Limite diario de saques atingido, tente em data posterior.")
        else:
            saque = float(input("Qual o valor do saque? "))
            if saque > limite_s:
                print("Saque n�o permitido, valor acima do limite.")
            elif saque > saldo:
                print("Saque n�o permitido, saldo insuficiente.")
            else:
                saldo -= saque
                n_saque += 1
                print(f"Saque de R${saque:.2f} realizado com sucesso.")
    
    # Extrato
    elif opt == "e":
        print(f"""
Extrato:
Saques Di�rios: {n_saque}
Saques Ainda Permitidos: {limite_diario - n_saque}
Saldo Dispon�vel: R${saldo:.2f}
""")
    
    # Sair
    elif opt == "q":
        break
    
    else:
        print("Opera��o inv�lida\nSelecione novamente a opera��o desejada.")
quit