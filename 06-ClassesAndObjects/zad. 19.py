class Konto():
    def __init__(self,numer):
        self.numer=str(numer)
        self.numer=(self.numer[0:2]+" "+self.numer[2:6]+" "+self.numer[6:10]+" "+self.numer[10:14]+" "+self.numer[14:18]+" "+self.numer[18:22]+" "+self.numer[22:])
        self.saldo=0
    def status(self):
        print('Numer rachunku:',self.numer)
        print('Twoje saldo:',self.saldo,'\n')
    def wplata(self,ile):
        self.saldo+=ile
    def wyplata(self,ile):
        if ile<=self.saldo:
            self.saldo-=ile
        else:
            print('Brak wystarczających środków'+'\n')

moje_konto=Konto(11112222333344445555666677)
moje_konto.status()
moje_konto.wplata(30)
moje_konto.status()
moje_konto.wyplata(40)
moje_konto.status()     
