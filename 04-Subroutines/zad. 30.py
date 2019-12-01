import random

def losowa():
    print(random.randint(1,50))

def p_n():
    p=[]
    n=[]
    for i in range(1000):
        x=random.randint(1,50)
        if x%2:
            p.append(x)
        else:
            n.append(x)
    print('liczby parzyste stanowią: ', len(p)/1000,'%')
    print('liczny nieparzyste stanowią: ',len(n)/1000,'%')
    
losowa()
p_n()