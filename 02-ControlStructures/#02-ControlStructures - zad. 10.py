#02-ControlStructures - zad. 10

x=int(input('wprowadź liczbę całkowitą: '))

if x%2==0 and x>0:
      print('liczba {} jest parzysta i dodatnia'.format(x))
elif x==0:
    print('wprowadzona liczba to zero')
elif x%2==0 and x<0:
    print('liczba {} jest parzysta i ujemna'.format(x))
else:
    print('liczba {} jest nieparzysta'.format(x))