# n = int(input())
# if n>1:
#     for i in range(2, n):
#         if (n % i) == 0:
#             print("invalid")
#             break;
#     else:
#         print("prime")
# else:
#     print("greater then 1")

n = int(input())
m = int(input())
for i in range(n, m+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)

