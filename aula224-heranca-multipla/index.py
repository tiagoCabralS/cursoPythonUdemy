# Herança multipla
# Quer dizer que no python, uma classe pode estender
# Várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança Múltipla e mixins(classe que não faz parte daquela família)
# Log -> FileLog (FileLog herda de Log)
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog) (cliente herda tudo de pessoa e herda tudo de FileLog)
#
# Python 3 usa C3 superclass linearization para gerar o mro (method resolution order).
# Você não precisa estudar isso (é complexo)
# Para saber a ordem de chamada dos métodos use o método de classe Classe.mor()
# Ou o matributo __mro__(Dunder - Double Underscore)

class A:
    ...
    
    def quem_sou(self):
        print('A')


class B(A):
    ...
    
    # def quem_sou(self):
    #     print('B')


class C(A):
    ...
    
    def quem_sou(self):
        print('C')
        

class D(B, C): # Ao colocar B primeiro, existe uma grande chance do metodo de B ser chamado
    ...
    
    # def quem_sou(self):
    #     print('D')


d = D()
d.quem_sou()
# print(D.__mro__) # Retorna uma tupla
print(D.mro()) # Retorna uma lista (FAZEM A MESMA COISA)
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
