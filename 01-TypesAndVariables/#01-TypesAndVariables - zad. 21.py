#01-TypesAndVariables - zad. 21

c=input("Podaj temperaturę w stopniach Celsjusza: ")
c=int(c)
f=32+(9*c/5)
k=c+273.15

print('Temperatura {} stopni Celsjusza jest równa temperaturze {} stopni Fahrenheita i {} stopni Kelvina'.format(c,f,k)) 