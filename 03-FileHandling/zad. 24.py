with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/tablica_dwuwymiarowa.csv','w') as file:
    tablica_danych=[['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
    for każdy in tablica_danych:
        x=[]
        for każdy_w_każdym in każdy:
            print(każdy_w_każdym)
        