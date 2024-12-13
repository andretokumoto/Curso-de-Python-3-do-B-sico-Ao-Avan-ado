from functools import reduce

produtos = [
    {'nome ' : 'produto 3','preco': 12},
    {'nome ' : 'produto 1','preco': 15},
    {'nome ' : 'produto 2','preco': 120},
]

def func_reduce(acumulador, produto):
    print('acumulador',acumulador)
    print('produto',produto)
    print
    return acumulador + produto['preco']
    

total = reduce(
    func_reduce,
    produtos,
    0
)

print()
print('total: ',total)