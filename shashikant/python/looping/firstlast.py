n = int(input())
last = n % 10
rev = 0

while n > 0:
   r = n % 10
   rev = (rev * 10) + r
   n = n // 10



first = rev % 10
print(first + last)


