#02-ControlStructures - zad. 11

login="marek"
password="m-123"

x=input('Podaj login: ')
y=input('Podaj hasło: ')

if x!=login or y!=password:
    print('Podałeś nieprawidłowe dane')
else:
    print('Witaj {}!'.format(login))