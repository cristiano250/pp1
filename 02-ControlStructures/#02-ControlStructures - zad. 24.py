#02-ControlStructures - zad. 24

imiona=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']
x=0
y=0
for i in range(len(imiona)):
   if len(imiona[i])>x:
       x=len(imiona[i])
       y=i
print('Najdłuższe imię w tablicy to: {}, składa się z {} znaków'.format(imiona[y],x))

