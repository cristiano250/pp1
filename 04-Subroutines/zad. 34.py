def nfib(n):    
    if n==0:
        return 0
    if n==1:
        return 1
    if n>1:
        return nfib(n-1)+nfib(n-2)

print(nfib(20))

for i in range(20):
    print(nfib(i),end=" ")
