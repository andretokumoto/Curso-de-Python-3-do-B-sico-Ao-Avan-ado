#set usa a logiaca de conjuntos matematicos

s1 = set('andre')
print(s1,type(s1))
s1 = {'andre','filipe'}
print(s1,type(s1))

#sets removem valores duplicados

#metodos add, update, clear e discard

s2 = set()
s2.add('Tokumoto') #so´adiciona um valor por vez
print(s2)
s2.update(('andre',1,2,3))#pode dser usado para mandar varios valores
print(s2)
s2.discard('Tokumoto')#elimina o valor passado
print(s2)
s2.clear()#limpa o set
print(s2)

#conjuntos em sets

#union
s2.update(('Palmeiras',1914,1999,1951,2020,2021,'andre'))
s3 = s1 | s2
print(s3)

#intersecção
s3 = s1 & s2
print(s3)

#diferenças
s3 = s2 - s1
print(s3)
s3 = s1 ^ s2 #diferença simetrica, apenas itens fora da intersecção
print(s3)