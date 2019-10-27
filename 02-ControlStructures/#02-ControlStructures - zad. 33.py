#02-ControlStructures - zad. 33

tab=['zero','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć']

word=input("Podaj słowo: ")

for i in range(0,len(word)):
    print(tab[int(word[i])],end=" ")
