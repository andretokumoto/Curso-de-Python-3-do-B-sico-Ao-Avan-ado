caminho = 'exemplo_arquivo.txt'

'''
arquivo = open(caminho,'w')
arquivo.write('texto do arquivo')
arquivo.close()
'''

with open(caminho,'w', encoding='utf-8') as arquivo:
    arquivo.write('Antenção:\n')
    arquivo.write('Texto com with open\n')
    arquivo.writelines(
        ('linha 1\n','linha 2\n')
    )
 
with open(caminho,'r') as arquivo:   
    arquivo.seek(0, 0)

    print('READLINES')
    for linha in arquivo.readlines():
        print(linha.strip())