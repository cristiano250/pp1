#01-TypesAndVariables - zad. 14
liczby=[2,7,3,5]

#punkt a
print(liczby[1])
#punkt b
i=0
sum=0
while i<len(liczby):
    sum=sum+liczby[i]
    i+=1
print(sum)
#punkt c
print(len(liczby))
#punkt d
print(liczby[len(liczby)-2])
#punkt e
print(sum/len(liczby))
