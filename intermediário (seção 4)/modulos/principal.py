import importlib

import modulo

for i in range(10):
    importlib.reload(modulo)
print('CABO')