# Salvando dados python em JSON com módulo json
import json

pessoa = {
    'nome': 'Tiágo Cabral',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.7,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# ENsure_ascii faz os caracteres de acento aparecerem
with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa, 
        arquivo, 
        ensure_ascii=False, 
        indent=2
    ) 

with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    print(pessoa['altura'])
