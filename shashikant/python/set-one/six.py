n = int(input("enter the number:"))
m = int(input("enter the number:"))
l = int(input("enter the number:"))
if n >= m and n >= l:
    print(n)
elif m >= n and m >= l:
    print(m)
else:
    print(l)