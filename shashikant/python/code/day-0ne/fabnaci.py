n = int(input("number :"))

a = 0
b = 1
if n == 1:
    print("0")
elif n == 2:
    print("1, 1")
else :
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c


