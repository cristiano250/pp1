with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/students.txt','w') as file:
    file.write('first_name,last_name,age,gender,email\n')
    file.write('Decca,Blackstone,52,Male,dblackstone0@time.com\n')
    file.write('Elena,Rechert,27,Female,erechert1@ucoz.com\n')
    file.write('Bibbye,Norree,26,Female,bnorree2@reddit.com\n')
    file.write('Alasdair,McCoole,53,Male,amccoole3@foxnews.com\n')
    file.write('Hogan,Hatrey,26,Male,hhatrey4@zimbio.com\n')
    
with open('C:/Users/Krystian/Desktop/pp1/03-FileHandling/students.txt','r') as file:
    tablica=[]
    for kazda_linia in file:
        tablica.append(kazda_linia.split(','))
    
#for kazdy_wiersz in tablica:
#   print(kazdy_wiersz)

for i in range(1,len(tablica)):
    if int(tablica[i][2])<30:
        x=(tablica[i][0],tablica[i][1],tablica[i][4])
        for i in x:
            print(f'{i:9}',end="")
    