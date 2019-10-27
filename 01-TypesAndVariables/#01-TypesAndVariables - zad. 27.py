#01-TypesAndVariables - zad. 27
from math import gcd

a=int(input("wprowadź pierwszą liczbę naturalną: "))
b=int(input("wprowadź drugą liczbę naturalną: "))

dzielnik=gcd(a,b)

if (a and b)>0:
    print('Największy wspólny dzielnik to: {}'.format(dzielnik))
else:
    print("Wprowadzone liczby nie są liczbami naturalnymi")