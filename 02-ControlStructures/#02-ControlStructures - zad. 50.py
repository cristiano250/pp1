#02-ControlStructures - zad. 50

x=int(input("Podaj liczbę: "))
y=x
tab=[]
while x>=1:
    if x%2==0:
        tab.append(0)
        x=x//2
    else:
        tab.append(1)
        x=x//2

print("Podana liczba {}(10) to binarnie: ".format(y),end='')
for i in range(len(tab)):
    print(tab[-i],end="")