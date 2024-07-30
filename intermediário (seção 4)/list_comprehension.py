import pprint


def p(valor):
    pprint.pprint(valor)


# cria um for e atribui valores na lista em sua declaração
lista  =[numero for numero in range(10)]
print(lista)

#pode ser aplica uma logica
lista  =[numero*10 for numero in range(10)]
print(lista)
print("")

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco' : produto['preco']*0.9}
    for produto in produtos
    if produto['preco'] <= 20.0
]

#print (*novos_produtos, sep='\n')
print("")

p(novos_produtos)
print('')


for x in range(3):
    for y in range(3):
        lista.append((x,y))
        
p(lista)
print('')

lista = []

lista = [
    (x,y)
    for x in range(4)
    for y in range(4)
]

p(lista)
print('')

lista = [
    [(letra,y) for letra in 'Tokumoto']
    for y in range(4)
]
p(lista)