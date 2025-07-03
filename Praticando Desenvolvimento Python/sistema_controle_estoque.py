''' Autor: André Holanda
    Projeto: Sistema de Controle de Estoque
    Data: 03/07/2025

    Descrição:
        Uma loja deseja um sistema que registre os produtos disponíveis em estoque e permita verificar se um produto solicitado está disponível.

    Entrada:
        - Lista de produtos em estoque.
        - Nome do produto solicitado.

    Saída:
        "Produto disponível" se o produto estiver no estoque.
        "Produto esgotado" caso contrário.
'''

# Lista de produtos disponíveis no estoque
estoque = ["Camiseta", "Calça", "Tênis", "Boné", "Jaqueta"]

# TODO: Verifique se o produto está no estoque:
def consulta_item(produto):
    if produto.title() in estoque:
        print("Produto disponível")
    else:
        print("Produto esgotado")

while True:
    # Entrada do usuário
    produto = input("Informe o nome do produto: ").strip()

    # Chamando a função de consulta
    consulta_item(produto)

    if "s" in input("\nNova Consulta (s):"):
        continue
    else:
        print("\nVocê não digitou 's' para realizar uma nova consulta."
              "\nSistema encerrado")
        break