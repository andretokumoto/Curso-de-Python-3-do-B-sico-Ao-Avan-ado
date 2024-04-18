"""
 DocString
"""
'''
 DocString
'''

#python tem typagem fore e dinâmica

def tipos_dados():
    
    #aspas simples
    print('simples')
    print('"aparece as aspas"')
    
    #aspas duplas
    print("duplas")
    
    #escape
    print("caractere \" escape")
    
    #r
    print(r"caractere \" escape")
    
    print(11) #int
    print(-11) #int
    print(11.0) #float
    
    #print do tipo
    
    print(type(11),type(11.0))
    
    #boolean
    print(10 == 10)  # Sim => True (Verdadeiro)
    print(10 == 11)  # Não => False (Falso)
    print(type(True))
    print(type(False))
    print(type(10 == 10))
    print(type(10 == 11))
    
def conversao_tipos():
    
    print("conversao")
    print(int('1'), type(int('1')))
    print(type(float('1') + 1))
    print(bool(' '))
    print(str(11) + 'b')

def variaveis():
    
    print("variaveis")
    nome = 'Andre'
    idade = 17
    maior_de_idade = idade >= 18
    print('Nome:', nome, 'Idade:', idade)
    print('E maior?', maior_de_idade)            
 
def operadores_aritmeticos():
    
    print('operadores')
    adicao = 10 + 10
    print('Adicao', adicao)

    subtracao = 10 - 5
    print('Subtracao', subtracao)

    multiplicacao = 10 * 10
    print('Multiplicacao', multiplicacao)

    divisao = 10 / 3  # float
    print('Divisao', divisao)

    divisao_inteira = 10 // 3
    print('Divisao inteira', divisao_inteira)

    exponenciacao = 2 ** 10
    print('Exponenciacao', exponenciacao)

    modulo = 55 % 2  # resto da divisão
    print('Modulo', modulo)     
    
tipos_dados()
conversao_tipos()
variaveis()
operadores_aritmeticos()