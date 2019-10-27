#02-ControlStructures - zad. 37
a=int(input("Podaj wartość a: "))
b=int(input("Podaj wartość b: "))
c=int(input("Podaj wartość c: "))

if a>c and a<b:
    print("Mediana to: ",a)
elif b>a and b<c:
    print("Mediana to: ",b)
elif c>b and c<a:
    print("Mediana to: ",c)