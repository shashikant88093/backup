n, k = map(int, input().split())
for i in range(n+1, k):
  if i % 2 == 1:
    print(i)
    print("\t")