#02-ControlStructures - zad. 14

x=int(input('Podaj wiek psa: '))

if x<=2:
    print('Wiek psa w psich latach to: {} lata'.format(x*10.5))
elif (x>2):
    print('Wiek psa w psich latach to: {} lata'.format(((x-2)*4)+(2*10.5)))