def mediana(tab):
    tab.sort()
    n=len(tab)
    if n%2!=0:
        print('Mediana to: ',tab[int(((n-1)/2))])
    else:
        print('Mediana to: ',(tab[int((n-2)/2)]+tab[int(n/2)])/2)


def dominanta(tab):
    for i in range(len(tab)):
        if tab[i]



tab=[4,3,1,5,4]
mediana(tab)
