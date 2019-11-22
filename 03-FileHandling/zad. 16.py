import re
komunikat = 'wtorek - 23C, środa - 21C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
srednia_temperatura=0
for kazda_temperatura in cyfry:
    srednia_temperatura+=int(kazda_temperatura)
print('Średnia temperatura na najbliższe dni wynosi:',srednia_temperatura/len(cyfry))