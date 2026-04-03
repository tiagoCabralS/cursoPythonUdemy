# O que são dataclasses
# O módulo dataclasses fornece um decorador e funções para criar métodos como 
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuario
# Em resumo dataclasses são syntax sugar para criar classes normais
# __post_init__() é o método chamado logo em seguida do __init__()

from dataclasses import dataclass # <- decorator

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    
    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    

if __name__ == "__main__":
    p1 = Pessoa('Tiago', 'Cabral')
    print(p1)
    print(p1.nome_completo)
