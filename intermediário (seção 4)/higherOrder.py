def mensagem(msg, conteudo):
    return f'{msg}, {conteudo}'

def executa(funcao, *args):
    return funcao(*args)

info = executa(mensagem, 'uma mensagem:','essa eh a mensagem')
print(info)