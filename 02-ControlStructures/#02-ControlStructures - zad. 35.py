#02-ControlStructures - zad. 35
from math import sqrt

print("Funkcja ma postać: ax2+bx+c=0.")
a=int(input("Podaj wartość a: "))
b=int(input("Podaj wartość b: "))
c=int(input("Podaj wartość c: "))

delta=(b**2)-(4*a*c)
if delta<0:
    print("Funkcja nie ma miejsc zerowych")
elif delta==0:
    print("Funkcja ma jeden (podwójny) pierwiastek: {}".format(-b/2*a))
else:
    x1=(-b-sqrt(delta))/(2*a)
    x2=(-b+sqrt(delta))/(2*a)
    print("Funkcja ma dwa pierwiastki, x1= {}, x2={}".format(x1,x2))
