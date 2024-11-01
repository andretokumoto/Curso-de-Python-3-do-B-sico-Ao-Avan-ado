def fora(x):
    a = x
    
    def dentro():
        print('locals: ',locals())
        print('freeVars: ',dentro.__code__.co_freevars)
        return a
    return dentro

dentro1 = fora(34)
dentro2 = fora(55)

print(dentro1())
print()
print(dentro2())
print()
print('Globals: ',globals())


def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    
    return interna
c = concatenar("isso")
print(c(' mesmo'))
print(c(' , isso e aquilo'))
print(c(' ,isso isso isso'))