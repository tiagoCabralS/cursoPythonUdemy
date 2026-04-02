# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2025 
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

dados = {'nome': 'João', 'idade': 38}
p1 = Pessoa(Pessoa(**dados)) #DESEMPACOTAR O DICIONARIO: Cria a chave igual ao valor

print(print(vars(p1))) # vars() retorna o __dict__ (dicionario da instância)
