class Caneta:
    def __init__(self, cor):
        self._cor = cor  
        
    @property
    def cor(self):
        return f'Caneta {self._cor}, {self._cor} Caneta !'

    @cor.setter
    def cor(self, cor):
        self._cor = cor
        
caneta1 = Caneta('Azul')
print(caneta1.cor)
