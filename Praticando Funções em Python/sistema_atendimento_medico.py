''' Autor: André Holanda
    Projeto: Sistema de Atendimento Médico
    Data: 16/06/2025

    Descrição: Uma clínica médica quer automatizar seu sistema de atendimento. Crie uma função que organize os pacientes em ordem de prioridade com base na idade e na urgência do caso.

    Requisitos:
        Critérios de Prioridade:
            Pacientes acima de 60 anos têm prioridade.
            Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima.
            Os demais pacientes são atendidos por ordem de chegada.
        Entrada:
            Um número inteiro n, representando a quantidade de pacientes.
            n linhas seguintes, cada uma contendo os dados de um paciente no formato: nome, idade, status
            nome: string representando o nome do paciente.
            idade: número inteiro representando a idade do paciente.
            status: string que pode ser "urgente" ou "normal".
        Saída:
        A saída deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, no formato: Ordem de Atendimento: nome1, nome2, nome3, ...        
'''

# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
ordem_urgente = []
ordem_prioridade = []
ordem_normal = []
lista_atendimento = []

# Função para percorrer à lista de pacientes e clasifica por status (urgente, prioridade ou normal), em seguida classifica de acordo com a idade. Por fim cria uma lista única com os nomes na ordem
def criar_lista_atendimento():
    for nome, idade, status in pacientes:
        if status.lower() == "urgente":
            ordem_urgente.append((nome, idade))  # Armazena nome e idade
        elif idade > 60:
            ordem_prioridade.append((nome, idade))
        else:
            ordem_normal.append((nome, idade))

    # Ordena cada fila por idade, como o sorte ordena do menor para o maior, precisamos inverte a sinal da idade
    ordem_urgente.sort(key=inverte_idade)
    ordem_prioridade.sort(key=inverte_idade)
    ordem_normal.sort(key=inverte_idade)

    # Uma vez as filas ordenadas, adiciona os nomes à lista final
    for nome, _ in ordem_urgente:
        lista_atendimento.append(nome)
    for nome, _ in ordem_prioridade:
        lista_atendimento.append(nome)
    for nome, _ in ordem_normal:
        lista_atendimento.append(nome)

# Função para inverter o sinal da idade
def inverte_idade(paciente):
    return -paciente[1]

# TODO: Exiba a ordem de atendimento com título e vírgulas:

# Função que percorre a lista de nomes e imprimi.
def imprimir_lista_atendimento():
    impressao = "Ordem de Atendimento: "
    contador = 0
    for nome in lista_atendimento:
        if contador == 0:
            impressao = impressao + f"{nome}"
            contador += 1
        else:
            impressao = impressao + f", {nome}"
    print(impressao)


criar_lista_atendimento()
imprimir_lista_atendimento()