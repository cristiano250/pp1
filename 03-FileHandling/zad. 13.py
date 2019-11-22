tablica=[32,16,5,8,24,7]
with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/tablica.txt','w') as file:
    for kazdaLiczba in tablica:
        file.write(str(kazdaLiczba)+'\n')