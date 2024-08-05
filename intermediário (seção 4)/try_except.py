a =10
b = 0
#b = '0'

try:
  c = a / b
  
except ZeroDivisionError as e:
    print(e) 
    
except NameError as e:
    print(e) 
    
except (TypeError,IndexError) as erro:
   # print('Erro de tipagem')
    print(erro.__class__.__name__)
    
except Exception:
    print('ERRO DESCONHECIDO')