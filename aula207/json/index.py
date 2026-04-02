# JSON é uma estrutura de dados para que vc TRANSPORTE ou SALVE dados
# "TIPOS DE DADOS: boolean, number, null, string, array [grupo de valores], objeto{}"

import json
import os

pessoas = [
    {
        "nome": 'Maria',
        "sobrenome": 'Vieira',
        "idade": 25,
        "ativo": False,
        "notas": ['A', 'A+'],
        "telefones": {
        "residencial": "00 0000-0000",
        "celular": "00 0000-0000",
    }
    },
    {
        "nome": 'Joana',
        "sobrenome": 'Silveira',
        "idade": 90,
        "ativo": True,
        "notas": ['B', 'C+'],
        "telefones": {
        "residencial": "00 0000-0000",
        "celular": "00 0000-0000",
    }
    },{
        "nome": 'Ruan',
        "sobrenome": 'Galvao',
        "idade": 17,
        "ativo": False,
        "notas": ['F', 'F'],
        "telefones": {
        "residencial": "00 0000-0000",
        "celular": "00 0000-0000",
    }
    }
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(SAVE_TO, 'w') as file:
    json.dump(pessoas, file, indent=2)
    
print(json.dumps(pessoas, indent=2))

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(JSON_FILE, 'r') as file:
    pessoas = json.load(file)
    print(json.dumps(pessoas))


json_string = '''[{"nome": "Maria", "sobrenome": "Vieira", "idade": 25, "ativo": false, "notas": ["A", "A+"], "telefones": {"residencial": "00 0000-0000", "celular": "00 0000-0000"}}, {"nome": "Joana", "sobrenome": "Silveira", "idade": 90, "ativo": true, "notas": ["B", "C+"], "telefones": {"residencial": "00 0000-0000", "celular": "00 0000-0000"}}, {"nome": "Ruan", "sobrenome": "Galvao", "idade": 17, "ativo": false, "notas": ["F", "F"], "telefones": {"residencial": "00 0000-0000", "celular": "00 0000-0000"}}]'''

pessoas = json.loads(json_string) # Converteu a string (json) em um dicionário python
for pessoa in pessoas:
    print(pessoa['nome'])
