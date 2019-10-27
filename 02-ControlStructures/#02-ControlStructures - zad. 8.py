#02-ControlStructures - zad. 8

a=int(input("podaj pierwszą liczbę całkowitą: "))
b=int(input("podaj drugą liczbę całkowitą: "))

if a>b:
    print(a, 'jest większe od ',b)
elif b>a:
    print(b, 'jest większe od ',a)
else:
    print(a, 'i ',b,' są równe')