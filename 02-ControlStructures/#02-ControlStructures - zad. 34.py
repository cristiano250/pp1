#02-ControlStructures - zad. 34
PESEL=input("Podaj swój numer PESEL: ")

x=int(PESEL[:2])
rok=0
p=int(PESEL[9])
płeć=""

y=int(PESEL[2])

if y==8:
    rok=1800+x
elif y==2:
    rok=2000+x
elif y==0:
    rok=1900+x

if (p==0)or(p%2==0) :
    płeć="kobieta"
else:
    płeć="mężczyzna"
    

print('Wiek: ',2018-rok)
print('Płeć: ',płeć)
