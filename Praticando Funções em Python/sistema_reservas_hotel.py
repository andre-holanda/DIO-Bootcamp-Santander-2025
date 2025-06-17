''' Autor: André Holanda
    Projeto: Sistema de Reservas de Hotel
    Data: 17/06/2025

    Descrição: Uma pousada deseja automatizar seu sistema de reservas. Crie uma função que receba uma lista de quartos disponíveis e uma lista de reservas solicitadas. A função deve verificar quais reservas podem ser aceitas e quais devem ser recusadas por falta de disponibilidade.

    Requisitos:
        Entrada:
            Uma lista contendo os números dos quartos disponíveis.
            Uma lista contendo os números dos quartos solicitados pelos clientes.

        Saída:
            Uma mensagem informando quais reservas foram confirmadas e quais foram recusadas.    
'''

confirmadas = []
recusadas = []

def processar_reservas():
    global confirmadas
    global recusadas
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            quartos_disponiveis.remove(reserva)
            confirmadas.append(reserva)
        else:
            recusadas.append(reserva)

    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos: 
    

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()