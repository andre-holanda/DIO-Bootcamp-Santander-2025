''' Autor: André Holanda
    Projeto: Sistema Bancário V2
    Data: 15/06/2025

    Descrição: Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visulizar extrato. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

    Requisitos:
        Separar as funções e passar os argumentos (posição) ou (nome).
        Saque: 
            (Keyword only) arg: saldo, valor, extrato, limite, numero_saque, limite_saque.
            Retorno: saldo e extrato.
        Depósito:
            (Positional only) arg: saldo, valor, extrato.
            Retorno: saldo e extrato.
        Extrato:
            (Positional only e Keyword only) arg positional: saldo, arg keyword: extrato
        Cadastra Usuários:
            lista de usuarios compostos por: nome, data nascimento, CPF e endereço, o endereço é uma string => logradouro, numero - bairro - cidade/sigla estado. O CPF só pode conter números, e não pode ter CPF igual.
        Conta Corrente:
            lista de contas com agencia "0001" e conta "1, 2, 3, ...", um cliente pode ter mais de uma conta, mas uma conta pertecene somente a um cliente.

        
'''
import time

def menu():
    menu = ''' 
        === Sistema Bancário ===
          1 - Depositar
          2 - Sacar
          3 - Extrato
          4 - Cadastrar Cliente
          5 - Listar Clientes
          6 - Cadastrar Conta
          7 - Listar Contas
          9 - Sair

        "Escolha a operação desejada: (1, 2, 3, 4, 5, 6, 7 ou 9)"
    => '''
    
    return  input(menu)

def cadastrar_cliente(clientes, cpf, nome, data_nascimento, endereco):
    if clientes and cpf in clientes:
        print(f"\nCliente (CPF: {cpf}) já cadastrado")
    else:
        clientes[cpf] = {"NOME": nome, "DATA_NASCIMENTO": data_nascimento, "ENDERECO": endereco}
        print(f"\nCliente cadastrado com sucesso!")

    return clientes

def listar_clientes(clientes, contas):
    if clientes:
        for chave, dados_cli in clientes.items():
            print(f"CPF: {chave}")
            print(f"NOME: {dados_cli['NOME']}")
            print(f"DATA NASCIMENTO: {dados_cli['DATA_NASCIMENTO']}")
            print(f"ENDEREÇO: {dados_cli['ENDERECO']}")
            if contas:
                for chave2, dados in contas.items():
                    if chave == dados["CPF"]:
                        print(f"AGENCIA: {dados['AGENCIA']}, CONTA: {chave2}, TITULAR: {dados_cli['NOME']}")
            print("==========================")
    else:
        print("Não existe cliente cadastrado.")

def cadastrar_conta(contas, cpf, clientes):
    if cpf in clientes:
        if contas:
            contas[len(contas) + 1] = {"AGENCIA": "0001", "CPF": cpf}
        else:
            contas[len(contas) + 1] = {"AGENCIA": "0001", "CPF": cpf}
        print(f"\nConta do CPF: {cpf}, cadastrada com sucesso!")
    else:
        print(f"\nCPF: {cpf} não cadastrado")

def listar_contas(contas):
    if contas:
        for chave, dados in contas.items():
            print(f"CPF: {dados['CPF']}")
            print(f"AGENCIA: {dados['AGENCIA']}")
            print(f"CONTA: {chave}")
            print("==========================")
    else:
        print("Não existe cliente cadastrado.")

def deposito(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        print(f"\nDepósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n")
        extrato.append(f"Depósito: R$ {valor_deposito:.2f}, Data: {time.strftime('%d/%m/%Y %H:%M:%S')}")
    else:
        print("Valor inválido. Por favor, digite um valor positivo.\n")
    
    return saldo, extrato

def saque(*, saldo, valor_saque, extrato, limite, saques_diarios, ):
    if saques_diarios == 0:
            print("Limite de saques diários atingido.\n")
    else:
        
        if valor_saque <= limite:
            if valor_saque <= saldo:
                saldo -= valor_saque
                print(f"\nSaque realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n")
                extrato.append(f"Saque: R$ {valor_saque:.2f}, Data: {time.strftime('%d/%m/%Y %H:%M:%S')}")
                saques_diarios -= 1
            else:
                print("Saldo insuficiente para saque.\n")
                saques_diarios += 1
        else:
            print("Valor do saque excede o limite de R$ 500,00 por operação\n")
            saques_diarios += 1
    return saldo, extrato, saques_diarios

def exibir_extrato(saldo, /, *, extrato):
    if extrato:
        print("\n================ EXTRATO ================")
        for item in extrato:
            print(item)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=========================================")
    else:
        print("Nenhum movimentação realizada.\n")

def main():
    saldo = 0.0
    saques_diarios = 3
    extrato = []
    LIMITE_SAQUE_OPERACAO = 500.0
    clientes = {}
    contas = {}

    while True:
        opcao = menu()
        if opcao == "9":
            print("Sistema encerrado.")
            break
        elif opcao == "1":
            valor_deposito = float(input("Digite o valor para depósito: R$ ").replace(',', '.'))
            saldo, extrato = deposito(saldo, valor_deposito, extrato)
        elif opcao == "2":
            valor_saque = float(input("Digite o valor para saque: R$ ").replace(',', '.'))
            saldo, extrato, saques_diarios = saque(saldo=saldo, valor_saque=valor_saque, extrato=extrato, limite=LIMITE_SAQUE_OPERACAO, saques_diarios=saques_diarios)
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            cpf = input("Informe o seu CPF: ").replace(".", "").replace("-","")
            if cpf not in clientes:
                nome = input("Informe o seu nome completo: ")
                data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
                endereco = input("Informa o endereço (logradouro, numero - bairro - cidade/sigla estado): ")
                cadastrar_cliente(clientes, cpf, nome, data_nascimento, endereco)
            else:
                print(f"CPF: {cpf} já cadastrado!")
        elif opcao == "5":
            listar_clientes(clientes, contas)
        elif opcao == "6":
            cpf = input("Informe o CPF para cadastrar a conta: ").replace(".", "").replace("-", "")
            cadastrar_conta(contas, cpf, clientes)
        elif opcao == "7":
            listar_contas(contas)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

main()