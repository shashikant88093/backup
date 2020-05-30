import sys, string
n = int(input())
L = list(map(int, input().split()))
for i in range(len(L)) :
    print(L[i], i)
