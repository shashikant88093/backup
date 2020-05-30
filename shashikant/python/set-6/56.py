s = input()
a,n = 0,0
for c in s :
    if c.isalpha() :
        a += 1
    if c.isdigit() :
        n += 1
if a and n :
    print('Yes')
else :
    print('No')