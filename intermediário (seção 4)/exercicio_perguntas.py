# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto eh 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto eh 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto eh 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print('Bem vindo ao show do milhao da shoppe!!')
acertos = 0

for pergunta in range(len(perguntas)):
    mensagem_pergunta = str(pergunta+1)+'º pergunta: '
    print(mensagem_pergunta)
    print(perguntas[pergunta]['Pergunta'])
    print('opcoes: ')
    print(list(perguntas[pergunta]['Opções']))
    resposta_participante = input('Qual sua resposta?')
    print("")
    
    if resposta_participante == perguntas[pergunta]['Resposta']:
        print('Certa Resposta !!')
        acertos+=1
    else:
        print('ERRROU !!')

print(f'Voce acertou {acertos} perguntas !')
    
    