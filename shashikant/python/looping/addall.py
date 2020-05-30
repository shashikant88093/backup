n = int(input())

rev = 1
while n > 0:
    r = n % 10
    # rev = rev + r
    rev = rev * r
    n = n // 10

print(rev)
