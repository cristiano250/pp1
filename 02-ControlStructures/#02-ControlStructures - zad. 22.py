#02-ControlStructures - zad. 22

tab=[15,8,31,47,2,19]
sum=0
i=0
for n in range(len(tab)):
    if tab[n]%2!=0:
        i+=1
        sum+=tab[n]
print("Nasza tablica: ",tab)
print("Suma wszystkich nieparzystych liczb z tablicy wynosi: ",sum)
print("Średnia arytmetyczna liczb nieparzystych wynosi: ",(sum/i))