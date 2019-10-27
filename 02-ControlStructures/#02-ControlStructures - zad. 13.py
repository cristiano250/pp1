#02-ControlStructures - zad. 13

x=int(input('Podaj pierwszą współrzędną: '))
y=int(input('Podaj drugą współrzędną: '))

if (x==0 and y==0):
    print('punkt o podanych współrzędnych leży w początku układu współrzędnych')
elif (x >0 and y>0):
    print('punkt o podanych współrzędnych leży w pierwszej ćwiartce układu współrzędnych')
elif (x <0 and y>0):
    print('punkt o podanych współrzędnych leży w drugiej ćwiartce układu współrzędnych')
elif (x <0 and y<0):
    print('punkt o podanych współrzędnych leży w trzeciej ćwiartce układu współrzędnych')
elif (x >0 and y<0):
    print('punkt o podanych współrzędnych leży w czwartej ćwiartce układu współrzędnych')