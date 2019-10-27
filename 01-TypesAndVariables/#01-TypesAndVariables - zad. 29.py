#01-TypesAndVariables - zad. 29

from random import randint

komputer=randint(1,6)
user=int(input("Podaj ile oczek kostki wyrzucił komputer: "))

print('Zgadłeś: {}'.format(komputer==user),' , komputer wyrzucił: {}'.format(komputer))

while user!=komputer:
    komputer=randint(1,6)
    user=int(input("Podaj ile oczek kostki wyrzucił komputer: "))
    print('Zgadłeś: {}'.format(komputer==user),' , komputer wyrzucił: {}'.format(komputer))
