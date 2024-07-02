frase = "olha soh  ,o miranha"

lista_palavras = frase.split()
print(lista_palavras)

lista_palavras = frase.split(',')
print(lista_palavras)

lista_frases = []
for i, frase in enumerate(lista_palavras):
    lista_frases.append(lista_palavras[i].strip())
    
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)