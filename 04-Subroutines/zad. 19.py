def suma(n):
    if n==1:
        return n
    if n>1:
        return n+suma(n-1)

print(suma(500))