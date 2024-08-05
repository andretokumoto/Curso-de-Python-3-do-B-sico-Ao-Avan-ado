import importlib

from modulos.modulo import mostra

def imprime():
    print("aeee")
    
def imprime_a():
    for i in range(10):
        importlib.reload(mostra)
    print('CABO')
    
    