# Ler o JSON e recriar as instâncias de novo
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


caminho = 'C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\curso\\aula207\\a\\index.json'
with open(caminho, "r", encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])

print(p1.nome, p2.nome, p3.nome)
