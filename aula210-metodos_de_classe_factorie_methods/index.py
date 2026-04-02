# Métodos de classe
# São metodos onde "self" será "cls", ou sejs: ao invés de receber a instância no primeiro parâmetro, receberemos a própria classe

class Pessoa:
    ano = 2023 # atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod # Torna o metodo em MÉTODO DE CLASSE, podendo ser utilizado sem passar uma instância
    def metodo_de_classe(cls): # cls é o molde, faz referência a CLASSE
        print('Hey')
        
    @classmethod 
    def criar_com_50_anos(cls, nome): # Está função cria novas instâncias onde elas possuem 50 anos
        return cls(nome, 50) # FÁBRICA - cria uma nova instância
    
    @classmethod
    def criar_sem_nome(cls, idade): # Está função cria novas instâncias anônimas
        return cls('Anônima', idade)
        
p1 = Pessoa('João', 34)
p3 = Pessoa.criar_sem_nome(18)
p2 = Pessoa.criar_com_50_anos('Helena')
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()
