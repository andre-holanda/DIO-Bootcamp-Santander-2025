''' Autor: André Holanda
    Projeto: Sistema Bancário V3
    Data: 18/06/2025

    Descrição: Iniciar a modelagem do sistema bancário em POO. Adicionar classes para cliente e as operações bancárias: depósito e saque.

    Desafio: Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguiro modelo de classe UML a seguir:

    OBS.: Imagem do Diagrama na pasta.        
'''
# Importação das bibliotecas utilizadas
import time
from abc import ABC, abstractmethod, abstractproperty

# classe cliente
class Cliente():
    """Classe Cliente

    Parameters
    ---------------
    _endereco : str
        atributo endereço do cliente
    _conta : Conta
        atributo do tipo Conta, contem as informações de saldo, numero, agencia, cliente, historico
    
    Returns
    ---------------
    endereco: str
    conta: Conta
    """
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def contas(self):
        return self._contas

    # FIXME: melhorar a visualizar dos dados do cliente.
    def __str__(self):
        return f"{self.__class__.__name__}:\n{','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    """Classe PessoaFisica

    Parameters
    ---------------
    _cpf : int
        sequencia numérica do cpf
    _nome : str
        nome completo do cliente
    _data_nascimento: time
        data de nascimento no formato dd-mm-aaaa
    
    Returns
    ---------------
    cpf: int
    nome: str
    data_nascimento: time
    """
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento

    def __str__(self):
        return f"{self.__class__.__name__}:\n{','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Conta():
    def __init__(self, numero, cliente):
        self._saldo = 0.00
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    def __str__(self):
        return f"{self.__class__.__name__}:\n{','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    def sacar(self, valor):
        saldo = self.saldo
        
        if valor > saldo:
            print("\nSaldo insuficiente!")
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True
        else:
            print("\nValor inválido!")
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizadocom sucesso!")
            return True
        else:
            print("Valor inválido!")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    def __str__(self):
        return f"\nAgência: {self.agencia}\nC/C: {self.numero}\nTitular: {self.cliente.nome}"

    @property
    def limite(self):
        return self._limite
    
    @property
    def limite_saques(self):
        return self._limite_saques
    
    def sacar(self, valor):
        saques_realizado = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        if saques_realizado >= self.limite_saques:
            print("\nTotal de saques diários ultrapassado!")
        elif valor > self.limite:
            print("\nValor maior que o limite por operação!")
        else:
            return super().sacar(valor)
        
        return False
    
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": time.strftime('%d/%m/%Y %H:%M:%S'),
        })

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        transacao = conta.sacar(self.valor)

        if transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        transacao = conta.depositar(self.valor)

        if transacao:
            conta.historico.adicionar_transacao(self)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não cadastrado!")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não cadastrado!")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não cadastrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n========================= EXTRATO =========================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações!"
    else:
        for transacao in transacoes:
            if transacao['tipo'] == "Saque":
                extrato += f"\n{transacao['tipo']}: \t\tR${transacao['valor']:.2f} \tData: {time.strftime('%d/%m/%Y %H:%M:%S')} "
            else:
                extrato += f"\n{transacao['tipo']}: \tR${transacao['valor']:.2f} \tData: {time.strftime('%d/%m/%Y %H:%M:%S')} "
    
    print(extrato)
    print(f"\nSaldo: R${conta.saldo:.2f}")
    print("===========================================================")

def cadastra_cliente(clientes):
    cpf = input("Informe o CPF do cliente (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nCPF já cadastrado")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - barrio - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!")

def cadastra_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não cadastrado!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nConta cadastrado com sucesso!")

def listar_contas(contas):
    for conta in contas:
        print("=" * 50)
        print(str(conta))

def listar_clientes(clientes):
    for cliente in clientes:
        print("=" * 50)
        print(str(cliente))

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
    
    return  int(input(menu))

def main():
    clientes = []
    contas = []

    # Loop infinido para exibir o menu
    while True:
        opcao = menu()

        # função match que pega a opção escolhida pelo usuário e chama a função relacionada
        match opcao:
            case 1:
                depositar(clientes)
            case 2:
                sacar(clientes)
            case 3:
                exibir_extrato(clientes)
            case 4:
                cadastra_cliente(clientes)
            case 5:
                listar_clientes(clientes)
            case 6:
                numero_conta = len(contas) + 1
                cadastra_conta(numero_conta, clientes, contas)
            case 7:
                listar_contas(contas)
            case 9:
                print("\nSistema encerrado")
                break

main()