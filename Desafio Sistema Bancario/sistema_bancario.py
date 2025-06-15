''' Autor: André Holanda
    Projeto: Sistema Bancário

    Requisitos:
        Depósito:   1. Validar se está sendo informado um valor positivo
                    2. Inicialmente só terá um usuário, não tera várias contas
                    3. Todos os depósitos devem ser armazenados para serem exibidos no extrato

        Saque:      1. Permitir apenas 3 saques diários, com valor máximo de R$ 500,00 por saque
                    2. Caso não tenha saldo suficiente, exibir uma mensagem
                    3. Todos os saques devem ser armazenados para serem exibidos no extrato
        
        Extrato:    1. Exibir todos os depósitos e saques realizados
                    2. O valor deve ser exibido no formato R$ XXX.XX
'''
import time

saldo = 0.0
saques_diarios = 3
extrato = []
LIMITE_SAQUE_OPERACAO = 500.0

while True:
    print("Sistema Bancário".center(22, "-"))
    print(" 1 - Depositar")
    print(" 2 - Sacar")
    print(" 3 - Extrato")
    print(" 4 - Sair\n")

    opcao = input("Escola a operação desejada: (1, 2, 3 ou 4)")

    if opcao == "4":
        print("Sistema encerrado.")
        break
    elif opcao == "1":
        valor_deposito = float(input("Digite o valor para depósito: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n")
            extrato.append(f"Depósito: R$ {valor_deposito:.2f}, Data: {time.strftime('%d/%m/%Y %H:%M:%S')}")
        else:
            print("Valor inválido. Por favor, digite um valor positivo.\n")
    elif opcao == "2":
        if saques_diarios == 0:
            print("Limite de saques diários atingido.\n")
        else:
            valor_saque = float(input("Digite o valor para saque: R$ "))
            if valor_saque <= LIMITE_SAQUE_OPERACAO:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n")
                    extrato.append(f"Saque: R$ {valor_saque:.2f}, Data: {time.strftime('%d/%m/%Y %H:%M:%S')}")
                    saques_diarios -= 1
                else:
                    print("Saldo insuficiente para saque.\n")
                    saques_diarios += 1
            else:
                print("Valor do saque excede o limite de R$ 500,00 por operação\n")
                saques_diarios += 1
    elif opcao == "3":
        if extrato:
            print("Extrato do cliente:")
            for item in extrato:
                print(item)
            print()
        else:
            print("Nenhum registro no extrato.\n")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")