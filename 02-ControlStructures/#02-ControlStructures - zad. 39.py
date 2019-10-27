#02-ControlStructures - zad. 39

tab=[0,1]

for i in range(2,51):
    tab.append(tab[i-2]+tab[i-1])
print(tab)