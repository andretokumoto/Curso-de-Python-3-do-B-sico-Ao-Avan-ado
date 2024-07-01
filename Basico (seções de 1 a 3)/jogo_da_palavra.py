import string

def main():
    palavra_secreta = 'palmeiras'
    letras_achadas=''
    condição_saida = 0
    cont = 0
   
    while(condição_saida==0):
        
        tentativa = input('Digite uma letra:')
        cont +=1
        if len(tentativa) > 1:
            print('digite apenas uma letra!')
            continue
        
        if tentativa in '0123456789':
            print('digite apenas letras')
            continue
        
        if tentativa in palavra_secreta:
            for letra in range(len(palavra_secreta)):
                if palavra_secreta[letra] == tentativa or palavra_secreta[letra] in letras_achadas:
                    print(palavra_secreta[letra],end='')
                    if tentativa not in letras_achadas:
                        letras_achadas = letras_achadas+tentativa
                    condição_saida +=1
                else:
                    print('*',end='')
                    condição_saida = 0
        print()
    
    print(f'Ganhou a palavra é {palavra_secreta} \n e voce acertou em {cont} tentativas')    

main()        