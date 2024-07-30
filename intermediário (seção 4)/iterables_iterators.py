import sys

iterable = ['eu','tenho','_iter_']

#iterator = iterable.__iter__()
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print('-----')

#generator

lista = [n for n in range(10000)]
generator = (n for n in range(100)) #definida no uso do parenteses -> ( <- n for n in range(100) -> ) <-

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
print('------')


for i in range(50):
    print(next(generator))