from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    
def aumentar(valor,porcentagem):
    return round(valor * porcentagem, 2)
 
def muda_preco(produto):
    return {
        **produto,
        'preco': aumentar_10porcento(produto['preco'])
    } 
  
aumentar_10porcento = partial (
    aumentar,
    porcentagem = 1.1
)
 
produtos = [
    {'nome ' : 'produto 3','preco': 12},
    {'nome ' : 'produto 1','preco': 15},
    {'nome ' : 'produto 2','preco': 120},
]

novos_prd = [
    {**p, 'preco':aumentar(p['preco'],1.1)} for p in produtos
]

novos_prd2 = [
    {**p, 'preco':aumentar_10porcento(p['preco'])} for p in produtos
]

novos_prd_map = map(
    muda_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_prd)
print_iter(novos_prd2)
print(list(novos_prd_map))