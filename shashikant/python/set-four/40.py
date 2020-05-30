n = int(input())
L = [1,1]
a,b = 1,1
if n==1 :
    print('1')
elif n==2 :
    print('1 1')
else :
    for i in range(2,n) :
        c = a+b
        L.append(c)
        a,b = b,c
    print(*L)
