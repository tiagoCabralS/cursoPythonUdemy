# @property + @setter - getter e setter no modo Pythônico
# como getter
# p/ evitar quebrar código cliente
# p/ habilitar setter
# p/ executar ações ao obter um atributo
# Atributos que começa, com um ou dois underlines não devem ser usados fora da classe


class Caneta:
    def __init__(self, cor):
        # private protected:
        self._cor = cor # O UNDERLINE no inicio de um atributo
        # significa que este atributo NÃO DEVE SER UTILIZADO por outros desenvolvedores
        self._cor_tampa = None
    
    # Um método que se comporta como um atributo, usado para obter o valor. (não precisa de parenteses)  
    @property 
    def cor(self):
        return self._cor

    
    # Um método para definir o valor. Util para RESTRINGIR determinadas coisas
    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor


    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
        
        
caneta = Caneta('Azul')
caneta.cor = 'Rosa'

# Getter -> obter valor
print(caneta.cor)
