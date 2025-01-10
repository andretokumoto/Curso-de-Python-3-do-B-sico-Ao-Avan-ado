class Pessoa():
    
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def estudar(self):
        print(f'{self.nome} {self.sobrenome} está estudando\n')
        
p1 = Pessoa("Andre","Filipe")
print(p1.nome, p1.sobrenome)
print()
p1.estudar()

p2 = Pessoa('Geraldino','Macarena')
p2.estudar()