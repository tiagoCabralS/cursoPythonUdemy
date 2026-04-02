# __new__ e __init__ em Classes Python
# __new__ é o método responsavel por criar e retornar o novo objeto. Por isso, new RECEBE cls.
# __new__ DEVE RETORNAR o novo objeto!
# __init__ é o mpetodo por inicializar a instância. Por isso receve self.
# __init__ NÃO DEVE RETORNAR nada (None)!
# object é a superclasse de uma classe
class A:
    def __new__(cls, *args, **kwargs): 
        # Aqui pode-se realizar o que quiser antes de depois da ciração da instância
        print('Antes de criar a instância')
        instancia = super().__new__(cls) # Momento de criação da instância
        print('Depois')
        instancia.x = 123
        return instancia
    
    def __init__(self, x):
        print('Sou o init')
        
    def __repr__(self):
        return 'A()'
    
a = A(123)
print(a.x)