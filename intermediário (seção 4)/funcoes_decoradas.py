

def inverte_string(string):
    return string[::-1]

def is_string(string):
    if not isinstance(string, str):
        raise TypeError('Param is not String')
    
def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        
        resultado = func(*args,**kwargs)
        
        return resultado
    
    return interna

inverte_checa = criar_funcao(inverte_string)
inverte_str = inverte_checa('123')
print(inverte_str)