import os
# Criando arquivos com Python + Context Manager
# Usamos a função open para abrir um arquivo em python (ele pode ou não existir)
# modos: r (leitura), w (escrita), x (para criação), t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis: write, read (escrever e ler), writelines (escrever várias linhas), seek (move o cursor), readline (ler linha), readlines (ler linhas)
# Vamos falar mais sobre os modulos os, mas: 
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load 

caminho_arquivo = 'C:\\Users\\carro_akq51l3\\OneDrive\\Documentos\\Estudos\\CursoEmVídeo\\python\\django\\aula187\\' # No WINDOWS colocar duas barras invertidas em CAMINHOS
caminho_arquivo += 'aula116.txt'

# Quando souber que o arquivo não existe, abrir ele com um dos modos de escrita:
# arquivo = open(caminho_arquivo, 'w') # Sempre que abrir um arquivo. FECHAR ELE LOGO em seguida
 
# arquivo.close() # Sempre que abrir um arquivo. FECHAR ELE LOGO em seguida
# Context Manager: Quando você cria um objeto que tem os métodos para você abrir alguma coisa, fazer algo e fechar essa uma coisa, você tá criando um Context Manager pode se usar o 'with open()' ele abre e fecha o arquivo, não importa  o que ocorra.

"""with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0) # move o cursor para o começo do arquivo
    print(arquivo.read())
    
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')
    
    print('ReadLines')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines(): # readlines: retorna uma lista das linhas
        print(linha, end='')

print('-' * 40)
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())"""

# Passar o caminho do arquivo, o modo de operação e o encoding, ever quando trabalhar com arquivos
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo: # O modo de leitura ('w') apaga tudo que estava no arquivo antes e escreve denovo
    # O modo de append ('a') escreve no final do arquivo, adiciona texto, sem apagar o que estava antes
    # O parâmetro encoding=utf-8 seleciona a codificação correta para carácteres especiais
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.remove(caminho_arquivo)
# os.rename(caminho_arquivo, 'aula116-2.txt')
