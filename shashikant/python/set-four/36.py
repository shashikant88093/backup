s = input()
k = 0
for c in s :
    if c.isalnum() or c.isspace() or c=='_': k += 1
print(len(s)-k)