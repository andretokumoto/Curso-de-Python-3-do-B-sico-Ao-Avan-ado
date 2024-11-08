from itertools import count

c1 = count(step=100)

for i in c1:
    
    print(i)
    
    if i > 1000:
        break