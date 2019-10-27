#01-TypesAndVariables - zad. 26

wzrost=int(input("Podaj wzrost w cm: "))
waga=int(input("Podaj wagę w kg: "))

bmi=round(waga/((wzrost/100)**2),1)

if (bmi>=18.5) and (bmi<=24.9):
    print("Twoja waga jest prawidłowa")
else:
    print("Twoja waga jest nieprawidłowa")