def rysujWykres(nazwa,ile):
    i=0
    for kazdy in nazwa:
        print( print(f'{kazdy:12}'+ile[i]*'#',end=''))
        i+=1

nazwa = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
ile = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]
rysujWykres(nazwa,ile)