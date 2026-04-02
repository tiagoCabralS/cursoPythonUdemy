# super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class A:
    def __init__(self, atributo):
        self.atributo = atributo
    
    atributo_a = 'valor a'
    def metodo(self):
        print('A')


class B(A): 
    # B tem tudo que tem em A
    # B possui neste momento o atributo_a e o atributo_b 
    atributo_b = 'valor b'
    
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self): # Este metodo esta sobrepondo o metodo de A
        print('B')


class C(B): 
    # C tem tudo que tem em B
    # C possui o atributo_a, atributo_b e o atributo_c
    atributo_c = 'valor c'
    
    def __init__(self, *args, **kwargs): # Usar o *args e **kwargs quando não estiver nem ai para o que vai ser passado. Vai passar pras classes que foram herdadas.
        super().__init__(*args, **kwargs)
        print('EI, burlei o sistema')
        
    
    def metodo(self):
        # super().metodo() # Vai executar o metodo de B (Classe que está sendo herdada por C)
        # super(B, self).metodo() # Vai executar o metodo de A (Classe que está sendo herdada por B)
        # super(A, self).metodo() # object (vai dar erro pois object não possui este metodo)
        print('C')

c = C('atributo', 'qualquer')
print(c.atributo)
