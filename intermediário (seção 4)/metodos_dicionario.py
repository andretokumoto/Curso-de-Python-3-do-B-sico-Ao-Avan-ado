# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Fulano',
    'sobrenome': 'De Tal',
    'idade': 90,
}

print(len(pessoa))#numero de chaves do dicionario

print(pessoa.keys())#lista as chaves

print(list(pessoa.values()))#value

print(list(pessoa.items()))#item

#get
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)

#get
print(pessoa.get('altura','nao tem'))

#pop
'''ultima = pessoa.popitem()
print(ultima)'''

#update
pessoa.update({
    'nome':'outroNome',
    'sobrenome':'familiaA'
})

print(pessoa)

pessoa.update(nome='andre',sobrenome='Tokumoto',idade=27)
print(pessoa)

tupla = ('nome','Aquele'),('sobrenome','Aquele Mesmo'),('idade',7)
pessoa.update(tupla)
print(pessoa)
