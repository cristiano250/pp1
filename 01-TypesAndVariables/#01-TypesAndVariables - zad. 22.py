#01-TypesAndVariables - zad. 22

a=int(input("Podaj długość boku a: "))
b=int(input("Podaj długość boku b: "))
c=int(input("Podaj długość boku c: "))

p=(a+b+c)/2

from math import sqrt
s=sqrt(p*(p-a)*(p-b)*(p-c))

print('Pole trójkąta o bokach: {}, {}, {} wynosi: {}'.format(a,b,c,s))