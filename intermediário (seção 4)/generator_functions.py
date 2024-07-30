# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1
    print('continua')
    yield 2
    print('ainda')
    yield 3
    print('quase')
    return 'FOI'

gen = generator(n=0)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


'''
def generator(n=0, maximum=10):
    while True:
        yield n # yield palsa a execução da função
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=100)
for n in gen:
    print(n)
'''