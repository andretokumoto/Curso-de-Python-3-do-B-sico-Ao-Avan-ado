lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista2 = lista.copy()

def exibir(lista):
        
    for item in lista:
        print(item)

'''
esse trecho de código 

def ordena(item):
    return item['sobrenome']

lista.sort(key=ordena)

pode ser escrito com labda da forma abaixo
'''
lista.sort(key=lambda item: item['sobrenome']) #sort
exibir(lista)
    
print('sorted')    
l3= sorted(lista2, key=lambda item: item['nome'])#sorted
exit(l3)

