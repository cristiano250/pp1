with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/NoEducation.txt','r') as file:
    ktora_linia=1
    for line in file:
        print(ktora_linia,line, end='')
        ktora_linia+=1