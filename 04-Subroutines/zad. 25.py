def jestImie(imie,imiona):
    if imie in imiona:
        print('imię {} zawarte jest w wykazie imion'.format(imie))
    else:
        print('imię {} nie jest zawarte w wykazie imion'.format(imie))

imiona=['Janek','Zosia','Ania','Tomek']
imie='Janek'

jestImie(imie,imiona)