#02-ControlStructures - zad. 40
from random import randint
tab=[]
jeden=0
dwa=0
trzy=0
cztery=0
pięć=0
sześć=0
for i in range(100):
    tab.append(randint(1,6))
for j in tab:
    if j==1:
        jeden+=1
    if j==2:
        dwa+=1
    if j==3:
        trzy+=1
    if j==4:
        cztery+=1
    if j==5:
        pięć+=1
    if j==6:
        sześć+=1
print("Jeden: ",jeden)
print("Dwa: ",dwa)
print("Trzy: ",trzy)
print("Cztery: ",cztery)
print("Pięć: ",pięć)
print("Sześć: ",sześć)


