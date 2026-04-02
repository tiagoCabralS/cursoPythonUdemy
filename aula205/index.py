# Atributos de classe

class Pessoa:
    ano_atual = 2025 
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
    
p1 = Pessoa('João', 38)
p2 = Pessoa('Helena', 15)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_de_nascimento())
print(p2.get_ano_de_nascimento())
