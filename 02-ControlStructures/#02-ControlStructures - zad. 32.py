#02-ControlStructures - zad. 32

word=input("Podaj słowo: ")

for i in range(1,len(word)+1):
    print(word[-i],end="")

    