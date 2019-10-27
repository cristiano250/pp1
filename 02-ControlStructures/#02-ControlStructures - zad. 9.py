#02-ControlStructures - zad. 9

x=int(input('wprowadź liczbę całkowitą: '))

if x%2==0 and x!=0:
      print('liczba {} jest parzysta'.format(x))
elif x==0:
    print('wprowadzona liczba to zero')