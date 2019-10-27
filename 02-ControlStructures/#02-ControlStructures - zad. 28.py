#02-ControlStructures - zad. 28
a=int(input("Podaj wysokość: "))
b=int(input("Podaj długość: "))

print(b*'*')
for n in range(a-2):
    print('*',(b-4)*' ','*')
print(b*'*')
