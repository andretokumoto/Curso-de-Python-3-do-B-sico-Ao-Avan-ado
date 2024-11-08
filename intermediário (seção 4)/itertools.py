from itertools import combinations,permutations,product

pessoas = [
    'Gerson', 'Bob', 'Mercedes', 'Wellinsohn',
]

camisetas = [
    ['verde','branca'],
    ['M','G'],
    ['manga Longa','manga normal','regata'],
]

print(list(combinations(pessoas,2)))
print()
print(list(permutations(pessoas,2)))
print()
print(list(product(*camisetas)))