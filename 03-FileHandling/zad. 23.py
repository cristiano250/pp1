import re
with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/land.txt','r') as file:
    tablica_cyfr=re.findall('\d',file.read())
sum=0
for kazda_cyfra in tablica_cyfr:
    sum+=int(kazda_cyfra)
print(f'suma cyfr w tekście wynosi: {sum}')