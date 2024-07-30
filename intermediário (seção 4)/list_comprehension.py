
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
]

print (*novos_produtos, sep='\n')