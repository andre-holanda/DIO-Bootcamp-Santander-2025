''' Autor: André Holanda
    Projeto: Simulador de Carrinho de Compras
    Data: 14/06/2025

    Descrição: Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.
    
    Requisitos:
        Entrada
            Lista de produtos adicionados ao carrinho (cada um com nome e preço).
        Saída
            Lista dos produtos adicionados e o total da compra.
'''

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# TODO: Exiba os itens e o total da compra
# Laço para exibir todos os itens
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")

# Impressão do valor total do carrinho
print(f"Total: R${total:.2f}")