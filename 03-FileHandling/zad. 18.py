tablica_liczb=[]
with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    for line in file:
        tablica_liczb.append(int(line))
tablica_liczb.sort()
for każda_liczba in tablica_liczb:
    print(każda_liczba, end=" ")