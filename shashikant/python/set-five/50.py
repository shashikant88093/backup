n = int(input())
s = bin(n)[2:]
if s.count('1') == 1:
    print('yes')
else :
    print('no')
