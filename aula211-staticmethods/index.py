# @staticmethod são inuteis em python

class Classe:
    @staticmethod
    def funcao_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)
        # Essa função não pode usar o self nem o cls
        # Está dentro da classe por "organização"
