def sumaCyfr(n):
    if n<10:
        return n
    if n>=10:
        n1=n//10
        n2=n%10
        return n1+sumaCyfr

print(sumaCyfr(4))
print(sumaCyfr(24))
print(sumaCyfr(9))
print(sumaCyfr(10))
print(sumaCyfr(99))