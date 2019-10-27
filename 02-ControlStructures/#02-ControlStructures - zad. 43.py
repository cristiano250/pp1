#02-ControlStructures - zad. 43
a=int(input("Podaj liczbę: "))
b=int(input("Podaj liczbę: "))
c=int(input("Podaj liczbę: "))

if a>c and a<b:
    print(c,a,b)
elif b>a and b<c:
    print(a,b,c)
elif c>b and c<a:
    print(b,c,a)