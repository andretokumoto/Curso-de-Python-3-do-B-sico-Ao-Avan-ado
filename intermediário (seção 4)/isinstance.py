# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Andre'},
]

for item in lista:
    
    print(item, isinstance(item,set))
    
    if isinstance(item,(int,float)):
        print(f'numero: {item}',sep='\n')