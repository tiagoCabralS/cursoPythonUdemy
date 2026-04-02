# Classe = Molde (sem dados)
# Uma classe pode gerar várias instâncias
# Na classe o self é a própria instância
# Métodos em instâncias de classes Python
# Método é uma Função que está dentro da classe e usa o primeiro parâmetro (self) SEMPRE referênciar o self ao declarar um método!!!
# Hard coded = Algo que foi escrito diretamente no código

class Carro:
    def __init__(self, nome='Sei lá'):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} está acelerando!')
        
fusca = Carro('Fusca')
fusca.acelerar()
