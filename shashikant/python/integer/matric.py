# mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(mat[2][0])

def sqr(l):
    sqre = []
    for i in l:
        sqre.append(i**2)
    return sqre
number = list(range(1, 11))
print(sqr(number))
