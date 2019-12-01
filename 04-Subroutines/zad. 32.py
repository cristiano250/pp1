x=[[1,2,0],[0,0,3],[5,1,1]]

def macierz(x):
    for wiersz in x:
        for kazdy in wiersz:
            print(kazdy, end=" ")
        print()
        
macierz(x)

def transponowana(macierz):
    for wiersz in macierz:
        for kazdy in wiersz:
            print(kazdy, end=" ")
        print()

transponowana(macierz)