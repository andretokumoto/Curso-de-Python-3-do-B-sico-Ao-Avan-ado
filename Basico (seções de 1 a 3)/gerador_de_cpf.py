#valida um cpf
cpf_entrada = input('Digite um CPF no formato ###.###.###-## :')

divisao_cpf = cpf_entrada.split('-')
nove_digitos_iniciais=divisao_cpf[0]
digitos_finais=divisao_cpf[1]
verifica_iguais = 0


valor_digitos_centena = nove_digitos_iniciais.split('.')


valor_digitos=''
for j in range(3):
    valor_digitos = valor_digitos+valor_digitos_centena[j]


soma = 0
multiplicador = 10

for i in range(9):
    if valor_digitos[0] != valor_digitos[i]:
        #print(valor_digitos[0]+','+valor_digitos[i])
        verifica_iguais = 1
    soma = soma + (int(valor_digitos[i])*multiplicador)
    multiplicador -=1

resto_divisao = (soma*10)%11

if str(resto_divisao)==digitos_finais[0] and verifica_iguais==1:
    valor_digitos = valor_digitos + digitos_finais[0]
    soma = 0
    multiplicador = 11

    for i in range(10):
        soma = soma + (int(valor_digitos[i])*multiplicador)
        multiplicador -=1
            
    resto_divisao = (soma*10)%11

    if str(resto_divisao)==digitos_finais[1]:
        print('CPF valido!')
            
    else: print('cpf não passou na verificação')

else:
    print('cpf não passou na verificação')
