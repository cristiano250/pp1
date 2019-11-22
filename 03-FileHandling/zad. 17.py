import re
tekst="To be, or not to be, that is the question"
samogłoski=re.findall('[aeiouy]',tekst)
print('Suma samogłosek w tekście wynosi: ',len(samogłoski))