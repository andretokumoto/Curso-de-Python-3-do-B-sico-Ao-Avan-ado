x,y,*resto  = 1,2,3,4,5,6
print(x,y,resto)

def soma(*args):
    resultado = 0 
    for numero in args:
        resultado +=numero
       # print(numero)
    return resultado

print(soma(1,2,3,4,5,6))