''' Autor: André Holanda
    Projeto: Sistema de Gestão de Veículos
    Data: 20/06/2025

    Descrição: Implemente uma classe Veiculo que represente um carro com marca, modelo e ano. Crie um método que verifique se o carro é considerado antigo (mais de 20 anos).

    Desafio: 
        Entrada:
            * Marca, modelo e ano do veículo.
        Saída:
            * "Veículo antigo" se o carro tiver mais de 20 anos.
            * "Veículo novo" caso contrário.
'''
from datetime import datetime

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:
class Veiculo:
    """Classe Veiculo
        calsse que define as caracteristicas de um veículo.
    Parameters
    ---------------
    _marca : str
        atributo que informa a marca do veículo
    _modelo : str
        atributo que informa o modelo do veículo
    _ano: int
        atribudo que informa o ano do veículo

    Returns
    ---------------
    marca: str
    modelo: Conta
    ano: int
    """
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
    
    @property
    def marca(self):
        return self._marca
    
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def ano(self):
        return self._ano
    
    def __str__(self):
        return f"{self.__class__.__name__}:\n{','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
    # TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:
    @classmethod
    def verificar_antiguidade(self):
        """Metodo verificar_antiguidade
            Método que informa se um veículo é antigo ou novo, calculado o ano atual e o ano do veículo.
        Parameters
        ---------------
    
        Returns
        ---------------
        string
        """
        if (datetime.today().year - ano) > 20:
            return "Veículo antigo"
        else:
            return "Veículo novo"

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())