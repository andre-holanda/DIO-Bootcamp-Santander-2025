''' Autor: André Holanda
    Projeto: Sistema Bancário V4
    Data: 25/06/2025

    Descrição: implementar as funcionalidades (Decorador de log, Gerador de relatórios, Iterador personalizado)

    Desafio: 
        * Decorador de logo:
            Implemente um decorador que seja aplicado a todas as funções de transações(depósito, saque, criação de conta, etc). Esse decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação.
        * Gerador de relatórios:
            Crie um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas. Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos).
        * Iterador personalizado:
            implemente um iterador personalizado ContaIterador que permita iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc).
'''
# Bibliotecas utilizadas
import datetime
from abc import ABC, abstractmethod, abstractproperty
import functools

AGENCIA_PADRAO = "0001"
LIMITE_SAQUES_PADRAO = 2
LIMITE_VALOR_SAQUE_PADRAO = 500.00

# Classe Cliente
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

    def __str__(self):
        contas_numeros = [str(conta.numero) for conta in self.contas]
        return (f"{self.__class__.__name__}:\n"
                f"Endereço: {self.endereco}\n"
                f"Contas: [{', '.join(contas_numeros) if contas_numeros else 'Nenhuma conta'}]")
    
    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= LIMITE_SAQUES_PADRAO:
            print("\n Você ultrapassou o limite de transações por dia")
            return
        
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica
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
        cliente_inf  = super().__str__().splitlines()
        return (f"{cliente_inf[0]}\n"
                f"CPF: {self.cpf}\n"
                f"Nome: {self.nome}\n"
                f"Data Nascimento: {self.data_nascimento}\n"
                f"Endereço: {self.endereco}\n" 
                f"{'\n'.join(cliente_inf[2:])}")

# Classe Conta
class Conta():
    """Classe Conta

    Parameters
    ---------------
    _saldo : float
        saldo da conta
    _numero : int
        numero que identicica a conta do cliente
    _agencia : int
        Valor fixo que corresponde a agencia da conta
    _cliente : Cliente
        É o proprietário da conta
    _historico : Historico
        Lista do tipo Historico, que armazena todas as transações da conta
    
    Methods
    ---------------
    nova_conta()

    sacar()

    depositar()

    
    Returns
    ---------------
    cpf: int
    nome: str
    data_nascimento: time
    """
    def __init__(self, numero, cliente):
        self._saldo = 0.00
        self._numero = numero
        self._agencia = AGENCIA_PADRAO
        self._cliente = cliente
        self._historico = Historico()
    
    def __str__(self):
        return f"{self.__class__.__name__}:\nNúmero: {self.numero}\nAgência: {self.agencia}\nTitular: {self.cliente.nome}\nSaldo Atual: {self.saldo}"

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

# Classe ContaCorrente
class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self._limite = LIMITE_VALOR_SAQUE_PADRAO
        self._limite_saques = LIMITE_SAQUES_PADRAO
    
    def __str__(self):
        return f"\n{self.__class__.__name__}:\nAgência: {self.agencia}\nC/C: {self.numero}\nTitular: {self.cliente.nome}"

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

# Classe ContaInterador
class ContaInterador:
    def __init__(self, contas):
        self.contas = contas
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador < len(self.contas):
            conta = self.contas[self.contador]
            self.contador += 1
            return conta
        raise StopIteration

# Classe Historico
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            #"data": time.strftime('%d/%m/%Y %H:%M:%S'),
            "data": datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })

    def gerador_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                if transacao["tipo"].lower() == "saque":
                    yield f"{transacao['tipo']}: \t\tR${transacao['valor']:.2f} \t| Data: {transacao['data']}"
                else:
                    yield f"{transacao['tipo']}: \tR${transacao['valor']:.2f} \t| Data: {transacao['data']}"
    
    def transacoes_do_dia(self):
        data_atual = datetime.datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.datetime.strptime(transacao["data"], "%d/%m/%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes

# Classe Transacao
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Saque
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

# Classe Deposito
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

# Função log_transacao
def log_transacao(func):
    @functools.wraps(func)
    def log(*args, **kwargs):
        print("Início: ", datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'), func.__name__, "\n")
        func(*args, **kwargs)
        print("\nTérmino: ", datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'), func.__name__)
    return log

# Função filtrar_cliente
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# Função recuperar_conta_cliente
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

# Função depositar
@log_transacao
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

# Função sacar
@log_transacao
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

# Função exibir_extrato
@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")

    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não cadastrado!")
        return
    
    tipo_transacao = input("Informe o tipo da transação (saque ou deposito), ou em branco para busca tudo: ").strip()

    if not tipo_transacao:
        tipo_transacao = None
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n========================= EXTRATO =========================")
    for linha in conta.historico.gerador_relatorio(tipo_transacao):
        print(linha)

    print(f"\nSaldo: R${conta.saldo:.2f}")
    print("===========================================================")

# Função cadastra_cliente
@log_transacao
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

# Função cadastra_conta
@log_transacao
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

# Função listar_contas
@log_transacao
def listar_contas(contas):
    contador = 0
    for conta in ContaInterador(contas):
        if contador == 0:
            print("=" * 50)
            print(str(conta))
            print("=" * 50)
            contador += 1
        else:
            print(str(conta))
            print("=" * 50)

# Função listar_clientes
@log_transacao
def listar_clientes(clientes):
    contador = 0
    for cliente in clientes:
        if contador == 0:
            print("=" * 50)
            print(str(cliente))
            print("=" * 50)
        else:
            print(str(cliente))
            print("=" * 50)

# Função menu
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

# Função main
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