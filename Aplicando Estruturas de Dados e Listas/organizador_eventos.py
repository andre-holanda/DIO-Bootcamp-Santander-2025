''' Autor: André Holanda
    Projeto: Organizador de Eventos
    Data: 14/06/2025

    Descrição: Uma empresa quer criar um organizador de eventos que divida os participantes em grupos de acordo com o tema escolhido.
    
    Requisitos:
        Entrada
            Lista de participantes e o tema escolhido por cada um.
        Saída
            Dicionário agrupando os participantes por tema.
'''
# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()

    virgula = linha.rfind(",")

    participante = linha[:virgula].strip()
    tema = linha[virgula + 1:].strip()

    if tema in eventos:
        eventos[tema].append(participante)
    else:
        eventos[tema] = [participante]

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")