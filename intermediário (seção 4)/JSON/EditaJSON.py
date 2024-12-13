import json
arquivo_json = 'exemplo.json'

pessoa = {
    'nome': 'Andre',
    'sobrenome': 'Tokumoto',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open(arquivo_json, 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open(arquivo_json, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])