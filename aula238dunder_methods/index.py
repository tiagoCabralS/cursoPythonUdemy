class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self): 
        # Para quem quer uma STRING do seu objeto
        return f'({self.x}, {self.y})'
    
    def __repr__(self): # Passa para OUTROS DESENVOLVEDORES a comunicação de 
        # como esses objetos foram criados  
        # Retorna a REPRESENTAÇÃO do objeto
        # class_name = type(self).__name__
        class_name = __class__.__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})' 
    # colocar o !r sempre que for mostrar as partes de desenvolvimento

p1 = Ponto(1, 2)
p2 = Ponto(978, 876)

print(p1)
print(repr(p2))
print(f'{p2!r}')