import random
class Kostka():
    def rzuc(self):
        return random.randint(1,6)
kostka1=Kostka()
kostka2=Kostka()
kostka3=Kostka()
suma=0
kostki=[kostka1,kostka2,kostka3]

for i in kostki:
    a=i.rzuc()
    print('Liczba wyrzuconych oczek: ',a)
    suma+=a
print('Suma wyrzuconych oczek to: {}'.format(suma))
    

