n = int(input())
L = list(map(int, input().split()))
L2 = sorted(L)
i = len(L) // 2
if len(L)%2 == 1 :
    print(L2[i])
else :
    print((L2[i-1]+L[i])/2)
