# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta = (1 + int(0.5 + 0.5)) ** (5 + 5)
print('resultado= '+ str(conta))

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')