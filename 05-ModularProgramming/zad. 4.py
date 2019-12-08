import math

x=3.7
y=4

sqrtx=math.sqrt(x)
print("Pierwiastek kwadratowy z {} wynosi: {}".format(x, sqrtx))

xdoy=math.pow(x,y)
print("{} do potęgi {} to: {}".format(x,y,xdoy))

pierwiastekyzx=math.pow(x,1/y)
print("Pierwiastek {}-tego stopnia z {} wynosi: {}".format(y,x, pierwiastekyzx))

pole=x*math.pi
print("Pole koła o promieniu {} wynosi: {}".format(x, pole))

silniay=math.factorial(y)
print("{} silnia to: {}".format(y, silniay))

najwiekszaMniejszaOdx=math.floor(x)
print("Największa możliwa liczba całkowita, mniejsza bądź równa {} to: {}".format(x, najwiekszaMniejszaOdx))