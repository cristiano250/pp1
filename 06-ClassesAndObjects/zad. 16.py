class book():
    def __init__(self,tytul,autor,liczba_stron):
        self.tytul=tytul
        self.autor=autor
        self.liczba_stron=liczba_stron
        self.biezaca_strona=1
        self.czy_otwarta=False
    def otworz(self):
        self.czy_otwarta=True
    def zamknij(self):
        self.czy_otwarta=False
    def dalej(self):
        if self.czy_otwarta==True:
            self.biezaca_strona+=1
        else:
            print('Książka jest zamknięta.')    
    def cofnij(self):
        if self.czy_otwarta==True:
            if self.biezaca_strona>1:
                self.biezaca_strona-=1
            else:
                ksiazka.zamknij()
        else:
            print('Książka jest zamknięta.')
    def status(self):
        if self.czy_otwarta==True:
            print('Autor: {}, Tytuł: {}, Liczba stron: {}, Bieżąca strona: {}'.format(self.tytul,self.autor,self.liczba_stron, self.biezaca_strona))
        else:
            print('Książka jest zamknięta.')
ksiazka=book('Potop','Sienkiewicz',400)
ksiazka.status()
ksiazka.otworz()
ksiazka.status()
ksiazka.dalej()
ksiazka.status()
ksiazka.dalej()
ksiazka.dalej()
ksiazka.status()
ksiazka.cofnij()
ksiazka.status()
ksiazka.cofnij()
ksiazka.status()
ksiazka.cofnij()
ksiazka.status()
ksiazka.cofnij()
ksiazka.status()
ksiazka.cofnij()
ksiazka.status()