def criar_multiplicador(multiplicador):
    print(multiplicador)
    def multiplicar(numero):
        print(numero)
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(7))
print(quadruplicar(2))