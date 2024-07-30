#yield from

def gen1():
    
    yield 1
    yield 2
    yield 3
    
def gen2(gen):
    
    yield from gen() #continua de onde gen1 parou
    yield 4
    yield 5
    

g = gen2(gen1)

for num in g:
    print(num)