#02-ControlStructures - zad. 12

x=int(input('Podaj pierwszą liczbę całkowitą: '))
y=int(input('Podaj drugą liczbę całkowitą: '))

if (x<0 and y<0):
    print('wprowadzone liczby {} i {} są ujemne'.format(x,y))
elif (x <0 or y<0):
    if x<0:
        print('wprowadzona liczba {} jest ujemna'.format(x))
    else:
        print('wprowadzona liczba {} jest ujemna'.format(y))
