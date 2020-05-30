n = int(input())
m = int(input())
if n > m:
    greater = n
else:
    greater = m
while(True):
     if((greater % n == 0) and (greater % m == 0)):
         lcm = greater
         break
     greater += 1

print(lcm)


