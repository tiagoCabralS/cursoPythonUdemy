class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
        
class Motor:
    def __init__(self, nome):
        self.nome = nome
        
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        
civic = Carro('civic')
honda = Fabricante('Honda')
m1 = Motor('M1')
civic.fabricante = honda
civic.motor = m1

print(f'O {civic.nome} é do fabricante {civic.fabricante.nome} e possui o motor {civic.motor.nome}')

fiat = Fabricante('Fiat')
m1 = Motor('M1')
uno = Carro('Uno')
uno.fabricante = fiat
uno.motor = m1

print(f'O {uno.nome} é do fabricante {uno.fabricante.nome} e possui o motor {uno.motor.nome}')