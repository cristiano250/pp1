#02-ControlStructures - zad. 47
a=int(input("Podaj kwotę: "))

pięć=0
dwa=0
jeden=0

pięć=a//5
reszta5=a%5

dwa=reszta5//2
reszta2=reszta5%2

jeden=reszta2

print("Kwota {} w monetach:".format(a))
print("5zł - {}".format(pięć),"szt")
print("2zł - {}".format(dwa),"szt")
print("1zł - {}".format(jeden),"szt")

        