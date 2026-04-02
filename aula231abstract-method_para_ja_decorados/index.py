from abc import ABC, abstractmethod

class AbstractFoo(ABC): # Algo abstrato que está na minha cabeça, não é para ser usado por fora
    def __init__(self, nome):
        self._nome = None
        self.nome = nome
        
    
    @property
    # Força o desenvolvedor utilizador da classe abaixo a criar a property
    # quando ela instanciar a classe abaixo
    def nome(self): 
        return self._nome
    
    @nome.setter
    @abstractmethod
    def nome(self, nome): ...


class Foo(AbstractFoo): # Algo CONCRETO
    def __init__(self, nome):
        super().__init__(nome) # sobrepondo o __init__ da classe herdada
        # print('Sou inútil')
    
    @AbstractFoo.nome.setter # Colocar o nome da superclasse(AbstractFoo) antes do nome do atributo, pois
    # ele não é dessa classe e sim da herdada
    def nome(self, nome):
        self._nome = nome
        
foo = Foo('Bar')
print(foo.nome)
