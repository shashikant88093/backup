n, k = map(int, input().split())
for i in range(n + 1,k):
    if i%2 ==0:
        if i != k - 1:
            print(i, end=" ")
        else:
            print(i)