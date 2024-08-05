# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from dados import produtos
import copy


new = [
        {**prod, 'preco': round(prod['preco']*1.1, 2)}
        for prod in copy.deepcopy(produtos)
      ]

print(produtos,sep='\n')
print()
print(new)


prod_ordenado_nome = sorted(
   copy.deepcopy(new),
   key= lambda p: p['nome']
)

print(prod_ordenado_nome)
print()

prod_ordenado_preco = sorted(
   copy.deepcopy(new),
   key= lambda p: p['preco']
)

print(prod_ordenado_preco)
print()