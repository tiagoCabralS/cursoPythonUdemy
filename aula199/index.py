class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
p1 = Pessoa('Tiago', 'Cabral')

print(p1.nome)
print(p1.sobrenome)
