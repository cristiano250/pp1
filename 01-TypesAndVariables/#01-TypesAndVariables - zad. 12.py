#01-TypesAndVariables - zad. 12
uczelnia="Uniwersytet Ekonomiczny w Krakowie"

#punkt a
print(uczelnia)
#punkt b
print(len(uczelnia))
#punkt c
print(uczelnia[0])
#punkt d
print(uczelnia[-1])
#punkt e
print(uczelnia[3:9])
#punky f
print(uczelnia[0:len("uniwersytet")]+uczelnia[-(len("w Krakowie")+1):])