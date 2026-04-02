# Encapsulamento (modificadores de acesso: public, protected, private)
# Python não tem modificadores de acessp
# Mas podemos seguir as seguintes convenções: 
# (sem underline) = public
# (um underline) = protected
#   não deve ser usada fora da classe ou suas subclasses
# (dois underlines) = private
#   só deve ser usado na classe em que foi declarado

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'
