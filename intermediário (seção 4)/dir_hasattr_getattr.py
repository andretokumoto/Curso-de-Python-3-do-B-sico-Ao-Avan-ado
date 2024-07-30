string = 'andre'
print(dir(string))

metodo = 'upper'
if hasattr(string, metodo):
    print(f'tem {metodo}')
    print(getattr(string,metodo))