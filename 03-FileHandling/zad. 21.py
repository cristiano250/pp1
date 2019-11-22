tablica=[]
with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/numbersinrows.txt','r') as file:
    for kazda_linia in file:
        x=(kazda_linia.split(','))
        for kazda_liczba_w_linii in x:
            tablica.append(kazda_liczba_w_linii)
print("W pliku jest {} liczb".format(len(tablica)))
sum=0
for kazda_liczba_w_tablicy in tablica:
    sum+=int(kazda_liczba_w_tablicy)
print("Suma wszystkich liczb w pliku to: ",sum)