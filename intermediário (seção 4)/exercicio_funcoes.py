def par_impar(numero):
    if numero%2 == 0: return 'Par'
    else: return 'impar'

def multiplica_valores(*args):
    total = 1
    for numero in args:
        total*=numero
    return total

def main():
    
    
    produto = multiplica_valores(1,45,3,9)
    paridade = par_impar(produto)
    
    print(f'o produto eh {produto} e esse valor eh {paridade}')
    
main()