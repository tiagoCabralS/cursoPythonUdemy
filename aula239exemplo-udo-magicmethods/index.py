class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def __repr__(self): # Passa para OUTROS DESENVOLVEDORES a comunicação de 
        # como esses objetos foram criados  
        # Retorna a REPRESENTAÇÃO do objeto
        # class_name = type(self).__name__
        class_name = __class__.__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})' 
        # colocar o !r sempre que for mostrar as partes de desenvolvimento

    def __add__(self, other): # Soma
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other): # Maior que (grater than))
        soma_self = self.x + self.y
        soma_other = other.x + other.y
        return soma_self > soma_other
    
if __name__ == '__main__':
    p1 = Ponto(4, 2) # 6
    p2 = Ponto(6, 4) # 10
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que p2:', p1 > p2)
    print('P2 é maior que p1', p2 > p1)