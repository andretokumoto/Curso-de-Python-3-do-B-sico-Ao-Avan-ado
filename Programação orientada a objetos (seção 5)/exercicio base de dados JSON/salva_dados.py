import json

caminho = 'base_dados.json'

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        

p1 = Pessoa('andre',28)
p2 = Pessoa("gargamel",233)
bd = [p1.__dict__,vars(p2)]

with open(caminho,'w') as arquivo:
    json.dump(bd,arquivo,ensure_ascii=False,indent=2)