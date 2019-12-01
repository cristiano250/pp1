import re
tekst="Hello World!"

def duzeLitery(tekst):
    duze=re.findall('[A-Z]',tekst)
    print(duze)
    
duzeLitery(tekst)