# Relações entre classes: associação, agregação e composição

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None
        
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Ferramenta:
    def __init__(self, nome):
        self.nome = nome
        
                
    def escrever(self):
        return f'{self.nome} está escrevendo'

escritor = Escritor('Jonas')
caneta = Ferramenta('Caneta Bic')
maquina_de_escrever = Ferramenta('Máquina')
escritor.ferramenta = caneta

print(caneta.escrever())
print(escritor.ferramenta.escrever())
print(maquina_de_escrever.escrever())