nome = "Fulano"
altura = 1.76
peso = 110
imc = peso/ (altura*altura)

mensagem = f'{nome} tem imc de {imc:.5f}'#f-string
formato = 'nome = {}  imc = {}'.format(nome,imc)

print(mensagem)
print(formato)