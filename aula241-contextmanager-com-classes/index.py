# Você pode implementar seus próprios protocolos apenas implementando os dunder methods que o python vai usar
# Isso é chamado de Duck Typing. Um conceito relacionado com tipagem dinâmica, 
# onde o python não está interessado no tipo, mas se alguns métodos existem,
# no seu objeto, para que ele funcione de forma adequada
# Duck Typing:
#   Quando vejo um passaro que caminha como um pato, nada como 
#   um pato e grasna como um pato, eu chamo aquele passaro de pato
# Para criar um context manager, os métodos __enter__ e __exit__ devem ser implementados.
# O método __exit__ receberá a classe de execução, a exceção e o traceback. 
# Se ele retornar True, exceção no with será suprimida.

# Ex:
# with open('aula149.txt', 'w', encoding='utf8') as arquivo:
#     ...

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo    
    
    def __exit__(self, classexception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
        
        # Recria a mesma exceção que seria levantada normalmente
        # raise classexception(*exception_.args).with_traceback(traceback_)
        
        # print(classexception)
        # print(exception_)
        # print(traceback_)
        
        # return True # Tratei a exceção
        # exception_.add_note('Minha nota')
        
        raise ConnectionError('Não deu para conectar.')

with MyOpen('aula242.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('with', arquivo)
