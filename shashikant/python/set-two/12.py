n = int(input("enter the value :"))
b = n
temp = 0
while n > 0:
    a = n % 10
    temp = temp * 10 + a
    n = n // 10
if temp == b:
    print("yes")
else:
    print("no")

