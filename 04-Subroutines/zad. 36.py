tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
def sumaElementow(tab):
    sum=0
    for kazdy_element_tablicy in tab:
        if isinstance(kazdy_element_tablicy, int):
            sum+=kazdy_element_tablicy
        else:
            sum+=sumaElementow(kazdy_element_tablicy)
    print(sum)
    
sumaElementow(tab)