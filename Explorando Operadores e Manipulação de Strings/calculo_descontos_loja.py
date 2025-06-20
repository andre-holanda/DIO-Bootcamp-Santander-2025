''' Autor: André Holanda
    Data: 13/06/2025
    Descrição: Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes.
    Regras de desconto:
        "DESCONTO10": 10% de desconto.
        "DESCONTO20": 20% de desconto.
        "SEM_DESCONTO": Sem desconto.
'''
# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Loop infinito
while True:
    preco = float(input("Informe o valor: ").strip())
    cupom = input("Digite o cupom de desconto: ").strip().upper()

    if cupom == "DESCONTO10":
        preco = preco - (preco * descontos["DESCONTO10"])
    elif cupom == "DESCONTO20":
        preco = preco - (preco * descontos["DESCONTO20"])
    elif cupom == "SEM_DESCONTO":
        preco = preco - (preco * descontos["SEM_DESCONTO"])
    else:
        print("Cupom inválido")

    print(f"{preco:.2f}")
    
    nova_consulta = input("Deseja informar novos valores? (S/N): ").strip().upper()
    if nova_consulta == "N":
        break

##################### Solução do desafio p/ passar no interpretador #####################
# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Solicita do usuário o preço e o cupom de desconto
preco = float(input().strip())
cupom = input().strip().upper()

# Condicional que identifica o cupom e realiza o calculo do desconto
if cupom == "DESCONTO10":
    preco = preco - (preco * descontos["DESCONTO10"])
elif cupom == "DESCONTO20":
    preco = preco - (preco * descontos["DESCONTO20"])
elif cupom == "SEM_DESCONTO":
    preco = preco - (preco * descontos["SEM_DESCONTO"])
else:
    print("Cupom inválido")

# Imprime na tela o preço com o desconto formatado com duas casas decimais
print(f"{preco:.2f}")