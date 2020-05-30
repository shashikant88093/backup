n = input()
n = int(n)
for i in range(0, n):
    if n % 2 == 0:
        print(n, n + 4)
    else:
        print(n, n - 3)