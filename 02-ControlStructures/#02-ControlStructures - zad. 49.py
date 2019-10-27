#02-ControlStructures - zad. 49
dni=['PN','WT','ŚR','CZW','PT','SB','ND']
j=int(input("Podaj pierwszy dzień miesiąca: "))

print('|'," | ".join(dni),'|')
for x in range(1 - j, 31):
    if x > 0:
        print(f'| {x:2} ', end='')
        if (x + j) % 7==0:
            print('|')
    else:
        print(f'|    ', end='')