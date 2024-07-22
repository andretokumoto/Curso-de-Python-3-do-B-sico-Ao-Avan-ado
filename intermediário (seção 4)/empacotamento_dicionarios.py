pessoa = {
    'nome': 'andre',
    'sobrenome':'tokumoto'
}

dados = {
    'idade':27,
    'altura':'177cm'
}

#desenpacotamento
a,b = pessoa.values()
c,d  = pessoa.items()
print(a,b)
print(c,d)

pessoaComDados = {**pessoa, **dados}#cria dicionario com todos os dados
print(pessoaComDados)

def mostra_kwargs(*args, **kwargs):
    print(kwargs)
    
mostra_kwargs(nome='andre', nacinalidade = 'brasileiro')
