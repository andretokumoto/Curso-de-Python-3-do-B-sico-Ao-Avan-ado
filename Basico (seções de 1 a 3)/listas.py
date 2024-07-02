lista = [1,2,3]
lista.append('string') #adiciona um item no final da lista
print(lista)

popDaLista = lista.pop() #remove um item do final da lista
print(popDaLista)

lista.append(4)
print(lista)
del lista[-2] #remove um item no index passado
print(lista)

lista.insert(1,0) #insere um item em uma posição especifica (posição,item a ser inserido)
print(lista)

lista2 = [10,11,12]

#modos de extender listas
lista3 = lista+lista2
print(lista3)

lista.extend(lista2)
print(lista)

#quando faz essa atribuição as duas variaveis estão apontando para o mesmo endereço de memoria
lista = lista2
print(lista)

lista[1] = 'valor'
print(lista2)

#copia o valor da lista em outro espaço de memória, tendo assim duas listas com o mesmo valor, mas com end diferentes
lista3 = lista.copy()
print(lista3)
lista3.pop()

print(lista)
print(lista3)

#desempacotamento
nome1,nome2,nome3 = ['Astolfo','Claudemiro','Bastiao']
print(nome3)

nome1,*resto = ['Astolfo','Claudemiro','Bastiao']
print(nome1)

nome1,*_ = ['Astolfo','Claudemiro','Bastiao']
print(nome1)

#tuplas

tupla = 'Astolfo','Claudemiro','Bastiao'
print(type(tupla))
