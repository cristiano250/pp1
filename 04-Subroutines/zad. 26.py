def podatek(dochod):
    if dochod<=5000:
        print('Należny podatek to:',dochod*0.17)
    else:
        print('Należny podatek to:',(5000*0.17)+(0.32*(dochod-5000)))

x=int(input("Podaj dochód: "))
podatek(x)