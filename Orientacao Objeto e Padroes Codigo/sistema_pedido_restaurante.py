''' Autor: André Holanda
    Projeto: Sistema de Pedido de Restaurante
    Data: 21/06/2025

    Descrição: Crie uma classe Pedido que represente um pedido em um restaurante, contendo os itens pedidos e um método para calcular o valor total da conta.

    Entrada:
        * Lista de itens e seus respectivos preços.
    Saída:
        * O valor total da conta.
'''
class Pedido:
    """Classe Pedido
        classe que define as caracteristicas para realizar um pedido no restaurante.
    Parameters
    ---------------
        Método adicionar_item
        Método calcular_total

    Returns
    ---------------
        valor_total: float
            somatório do valor, referente aos itens pedidos.
    """
    def __init__(self):
        self.itens = []

    # adicionar_item adiciona o nome e o preço do produto a lista de itens
    def adicionar_item(self, nome, preco):
        self.itens.append((nome, float(preco)))

    # calcular_total percorre a lista de itens e soma os preço, retornando o valor total do pedido
    def calcular_total(self):
        valor_total = 0.0
        for item in self.itens:
            valor_total += item[1]
        return valor_total
        
quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    pedido.adicionar_item(nome, preco)

total_pedido = pedido.calcular_total()
print(f"{total_pedido:.2f}")