#dicionarios em python funcionam mais ou menos como struct em C(?)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

pessoa = {
    'nome': 'Fulaninho',
    'sobrenome':'de Tal',
    'idade':'100',
    'endereço': [
      {'Rua':'Aquela lá','número':'1'},  
      {'Rua':'Dos Bobos','número':'0'}
    ],
}

print(f'{pessoa["nome"]}, {pessoa["sobrenome"]}, {pessoa["idade"]} anos, Mora em {pessoa["endereço"]}')

