tablica_parzystych=[]
with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    for kazda_linia in file:
        if int(kazda_linia)%2==0:
            tablica_parzystych.append(kazda_linia)
with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/evennumbers.txt','w') as file:
    for kazda_parzysta in tablica_parzystych:
        file.write(kazda_parzysta)
