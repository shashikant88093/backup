n = int(input())
L = []
while n :
    a = n%10
    L.append(a)
    n //= 10
L = L[::-1]
print(*L)