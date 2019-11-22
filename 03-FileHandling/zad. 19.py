tablica_nazw=[]
with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/universities.txt','r') as file:
    for kazda_linia in file:
        tablica_nazw.append(kazda_linia)
    tablica_nazw.sort()
with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/universities.txt','w') as file:
    for kazda_linia in tablica_nazw:
        file.write(kazda_linia)
    
    


