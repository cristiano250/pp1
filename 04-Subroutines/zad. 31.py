def reverse(tab):
    odwrocona=[]
    for i in range(len(tab)):
        odwrocona.append(tab[len(tab)-1-i])
    print(tab)
    print(odwrocona)
    
tab=[2,5,4,1,8,7,4,0,9]

reverse(tab)