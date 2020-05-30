# n = int(input())
# sum = n
# rev = 0
# while n > 0:
#     r = n % 10
#     rev = (rev * 10) + r
#     n = n // 10
# if sum == rev:
#     print(sum)
# else:
#     print("invalid")


n = int(input())
m = int(input())

for i in range(n, m + 1):
    temp = i
    rev = 0
    while temp > 0:
        r = temp % 10
        rev = (rev*10) + r
        temp = temp // 10
    if i == rev:
        print(i)