import sys, string
s = input()
if s[0] == '+' or s[0] == '-':
    s = s[1:]
if s[0] == '.':
    for i in range(1, len(s)):
        if not s[i].isdigit():
            print('No')
            sys.exit()
else :
    i=0
    while i<len(s) and s[i] != '.':
        if not s[i].isdigit():
            print('No')
            sys.exit()
        i += 1
    i += 1
    while i<len(s) :
        if not s[i].isdigit():
            print('No')
            sys.exit()
        i += 1
print('Yes')

