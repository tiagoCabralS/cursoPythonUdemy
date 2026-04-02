from log import LogPrintMixin, LogFileMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False
    
    def ligar(self):
        if not self._ligado:
            self._ligado = True
        
    def desligar(self):
        if self._ligado:
            self._ligado = False

class SmathPhone(Eletronico, LogFileMixin): # Usei a herança multipla para
    # colocar uma coisa que não é da família de eletronico dentro de smartphone
    # que vai adicionar uma funcionalidade a mais (Fazer Log)
    def ligar(self):
        super().ligar()
        
        if self._ligado:
            msg = f'{self._nome} está ligado.'
            self.log_success(msg)
        
    def desligar(self):
        super().desligar()
        
        if not self._ligado:
            msg = f'{self._nome} está desligado.'
            self.log_error(msg)