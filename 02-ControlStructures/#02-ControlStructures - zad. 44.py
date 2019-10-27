#02-ControlStructures - zad. 44
a=int(input("Podaj limit prędkości (km/h): "))
b=int(input("Podaj prędkość samochodu (km/h): "))

if b-a<=10:
    print("Mandat wynosi:",(b-a)*5,"zł")
else:
    print("Mandat wynosi:",50+((b-a)-10)*15,"zł")