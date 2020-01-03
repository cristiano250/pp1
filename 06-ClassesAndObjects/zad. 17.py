import math
class Ulamek():
    def __init__(self, licznik, mianownik):
        self.licznik=licznik
        self.mianownik=mianownik
    def show(self):
        print('Twój ułamek to: {}/{}'.format(self.licznik,self.mianownik))
    def uproszczony(self):
        nwd=math.gcd(self.licznik,self.mianownik)
        licznik=int(self.licznik/nwd)
        mianownik=int(self.mianownik/nwd)
        if licznik!=self.licznik:
            print('Twój ułamek uproszczony to: {}/{}'.format(licznik,mianownik))
ulamek=Ulamek(2,4)
ulamek.show()
ulamek.uproszczony()