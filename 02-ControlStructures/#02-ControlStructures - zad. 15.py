#02-ControlStructures - zad. 15

x=int(input('Podaj liczbę z zakresu od 1 do 10: '))

for i in range(1,11):
    print('{} x {} = {}'.format(x,i,x*i))