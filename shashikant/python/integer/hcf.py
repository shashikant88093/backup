n = int(input())
m = int(input())
if n > m:
    smaller = n
else:
    smaller = m
for i in range(1, smaller + 1):
    if (n % i == 0) and (m % i == 0):
        hcf = i
        print(hcf)