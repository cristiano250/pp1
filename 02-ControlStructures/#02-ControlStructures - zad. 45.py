#02-ControlStructures - zad. 45

n=int(input("Podaj liczbę szukanych liczb pierwszych: "))
tab=[]
j=2

while len(tab)<n:
    for i in range(2,j):
        if j%i==0:
            break
    else:
        tab.append(j)
    j+=1
print(tab)

  
