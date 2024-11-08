
def cria_decoradores(a,b):
    def cria_funcoes(func):
        print('decoradora 1')
        
        def aninhada(*args, **kwargs):
            print('aninhada')
            res = func(*args, **kwargs)
            return res
        
        return aninhada
    return cria_funcoes

@cria_decoradores(1,2)
def soma(x,y):
    return x + y

mult = cria_decoradores(1,2)(lambda x,y: x*y)

somar = soma(10,3)
multiplica = mult(8,10)
print(somar)
print(multiplica)

