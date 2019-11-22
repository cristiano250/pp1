with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    suma=0
    for liczby in file:
        suma+=int(liczby)
    print(suma)