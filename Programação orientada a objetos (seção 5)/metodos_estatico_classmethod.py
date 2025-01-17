class Conexao:
    
    def __init__(self,host='localhost'):
        self.host = host
        self.user = None
        self.password = None
        
    def set_user(self,user):
        self.user = user
        
    def set_password(self,password):
        self.password = password
        
    @classmethod
    def create_with_auth(cls, user,password):
        conection = cls()
        conection.user = user
        conection.password = password
        return conection
    
    @staticmethod
    def log(msg):
        print('LOG',msg)
    
    
    
c1 = Conexao.create_with_auth('Chefao','1234')
print(c1.user,c1.password)
print(Conexao.log('Super mensagem UAU'))