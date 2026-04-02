# JSON para salvar alguns tipos de sorvetes e suas notas
import json
"""
sorvetes = {
    'sabores': [
        'baunilha','chocolate','morango',
    ],
    'opinioes': [
        'Baunilha é uma delícia, mas eu ADOOOORO o pretão.',
        'Chocolate gostosinho.', 
        'baunilha uma delícia!',
        'Adorei o de morango, recomendo.',
    ],
}

with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\praticando\\sovetes.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        sorvetes,
        arquivo,
        ensure_ascii=False,
        indent=2,
    ) 
"""

with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\praticando\\sovetes.json', 'r', encoding='utf8') as arquivo:
    sorvetes = json.load(arquivo)
    sorvetes['sabores'].append('pistache')

with open('C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula191\\praticando\\sovetes.json', 'w') as arquivo:
    json.dump(sorvetes, arquivo, indent=2)

