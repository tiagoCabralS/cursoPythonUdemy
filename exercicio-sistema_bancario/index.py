from abc import ABC

class Conta(ABC):
    """ContaCorrente, ContaPoupanca (herdam de Conta)"""

class Pessoa(ABC):
    """Criar a classe cliente que herda de pessoa
    Cliente tem Conta (agregação)"""

class Banco:
    """Banco tem contas e clientes (agregação)"""

