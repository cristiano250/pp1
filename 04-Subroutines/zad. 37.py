tab=[2,3,1,2,5,6,4,5,6,3]

def unikat(tab):
    u=[]
    for i in tab:
        if tab.count(i)==1:
            u.append(i)
    print(u)
    
unikat(tab)