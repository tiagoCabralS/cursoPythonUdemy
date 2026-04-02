# Exercício: Salve sua classe em JSON, salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos (Faça em arquivos separados)
# Ciar o arquivo da base de dados
import json

caminho = 'C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\curso\\aula207\\a\\index.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Tiago', 18)
p2 = Pessoa('Joana', 77)
p3 = Pessoa('Melisa', 26)
bd = [vars(p1), p2.__dict__, vars(p3)]

with open(caminho, 'w', encoding='utf8') as arquivo:
    json.dump(bd, arquivo, indent=2)
