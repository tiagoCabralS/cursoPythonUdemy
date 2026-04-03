from abc import ABC, abstractmethod

class Conta(ABC):
    """ContaCorrente, ContaPoupanca (herdam de Conta)"""
    def __init__(self, agencia, num_conta, saldo=0):
        super().__init__()
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self): ...
    """A subclasses devem implementar este método (Polimorfismo)"""
    
    def depositar(self, valor):
        self.saldo += valor
        
class ContaPoupanca(Conta):
    def __init__(self, agencia, num_conta, saldo=0):
        super().__init__(agencia, num_conta, saldo)
        
    def sacar(self, valor, autenticacao: bool):
        if autenticacao:
            if valor <= self.saldo:
                self.saldo -+ valor
            else:
                print('Saldo insuficiente.')
        else:
            print('Cliente não encontrado.')

class ContaCorrente(Conta):
    def __init__(self, agencia, num_conta, saldo=0, limite=100):
        super().__init__(agencia, num_conta, saldo)
        self._limite = limite
        
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, valor):
        if valor >= 1:
            self._limite = valor
        else:
            print(f'Não é possível adicionar um limite de R${valor}')
            
    def sacar(self, valor, autenticacao: bool):
        if autenticacao:
            if valor <= self.saldo:
                self.saldo -= valor
            elif valor <= self.saldo + self.limite:
                valor -= self.saldo
                self.saldo = 0
                self.limite -= valor
            else:
                print('Saldo e limite insuficientes.')
        else:
            print('Cliente não encontrado.')

class Pessoa():
    """Criar a classe cliente que herda de pessoa
    Cliente tem Conta (agregação)"""
    def __init__(self, nome, idade):
        super().__init__()
        self._nome = nome
        self._idade = idade
    
    # getter
    @property
    def nome(self):
        return self._nome
    
    # getter
    @property
    def idade(self):
        return self._idade
    
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta: Conta):
        super().__init__(nome, idade)
        self.conta = conta

class Banco:
    """Banco tem contas e clientes (agregação)"""
    def __init__(self):
        self.agencias = []
        self.clientes = []
        self.contas = []
        
    def add_cliente(self, cliente: Cliente):
        self.clientes.append(cliente.nome)
        self.agencias.append(cliente.conta.agencia)
        self.contas.append(cliente.conta.num_conta)
        
    def autenticar(self, cliente: Cliente):
        agencia = False 
        clienty = False 
        conta = False

        if cliente.conta.agencia in self.agencias:
            agencia = True
        if cliente.conta.num_conta in self.contas:
            conta = True
        if cliente.nome in self.clientes:
            clienty = True
        
        if agencia and conta and clienty:
            return True
        else:
            return False

banco1 = Banco()

conta1 = ContaCorrente('0001', 9999, 1000, 500)
cliente1 = Cliente('Tiago', 18, conta1)

conta2 = ContaPoupanca('0002', 8888, 500)
cliente2 = Cliente('Joana', 39, conta2)

banco1.add_cliente(cliente2)
banco1.add_cliente(cliente1)

print('-' *40)
print(f"Agencia: {cliente1.conta.agencia}")
print(f"Número da conta: {cliente1.conta.num_conta}")
print(f"Saldo: {cliente1.conta.saldo}")
print(f"Limite: {cliente1.conta.limite}")
print('-' *40)

cliente1.conta.sacar(100, banco1.autenticar(cliente1))
print(f"Saldo: {cliente1.conta.saldo}")
print('-' *40)
print(f"Agencia: {cliente2.conta.agencia}")
print(f"Número da conta: {cliente2.conta.num_conta}")
print(f"Saldo: {cliente2.conta.saldo}")
print('-' *40)

print(banco1.autenticar(cliente2))
