# Context Manager com função - Criando e usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('ABRINDO ARQUIVO')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo # Torna a função um generator (retorna um generator)
    except Exception as e:
        print('Ocorreu um erro', e)
    finally:
        print('FECHANDO ARQUIVO')
        arquivo.close()

with my_open('aula243.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n', 123)
    arquivo.write('Linha 1\n')
    print('WITH', arquivo)
