# @property - um getter no modo pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# property é uma propriedade do objeto, ela é um método que se comporta como um atributo
# Geralmente é usada nas seguintes situações: 
# Como getter, p/ evitar quebrar código cliente, p/ habilitar setter, /p/ executar ações ao obter um atributo
# Código cliente é o código que usa o seu código

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        
    @property # Um método que se comporta como um atributo. (não precisa de parenteses)
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
        
    @property
    def cor_tampa(self):
        return 123456
    
caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)