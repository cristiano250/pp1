#02-ControlStructures - zad. 30

PIN="0805"

pin=input("Wprowadź kod PIN: ")
i=1
while pin!=PIN and i<3:
        print("Kod PIN jest niepoprawny")
        pin=input("Wprowadź kod PIN: ")
        i+=1
if pin==PIN and i<=3:
    print("kod PIN poprawny")
elif pin!=PIN and i==3:
    print("Karta została zablokowana")
            