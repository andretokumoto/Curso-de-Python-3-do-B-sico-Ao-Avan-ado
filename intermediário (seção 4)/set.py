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