n = int(input())
for i in range(1, n * 2):
    if n % 2 == 0:
        print(n*2)
        break
else:
    print(n + 2)
