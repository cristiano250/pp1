#02-ControlStructures - zad. 41
x=int(input("Podaj liczbę: "))
i=0
sum=0
sr=0
while x!=0:
    i+=1
    sum+=x
    sr=sum/i
    x=int(input("Podaj liczbę: "))
if x==0:
    print("REZULTAT: Wprowadzonych liczb: {}, SUMA: {}, Średnia: {}".format(i,sum,sr))