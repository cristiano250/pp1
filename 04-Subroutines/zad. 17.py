import random
def rzucKostka():
    x=random.randint(1,6)
    return x
sum=0
wyrzucone=[]
for i in range(3):
    wyrzucone.append(rzucKostka())
    sum+=wyrzucone[i]
print("Wyrzucone oczka to: ",wyrzucone)
print(sum)
