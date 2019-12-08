import csv
import statistics
age=[]
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row)
        age.append(row[2])
        for j in row:
            print(f'{j:14}',end="")
        print()
        
age.pop(0)
ageint=[]
for i in age:
    ageint.append(int(i))
srednia=statistics.mean(ageint)
print()
print('srednia wieku wynosi: {} lat'.format(srednia))

