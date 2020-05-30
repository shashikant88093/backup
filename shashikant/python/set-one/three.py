num = input("Enter the alphabet only : ")
vowel = ['a', 'e', 'i', 'o', 'u']
num = num.casefold()
if num >= 'a' and num <= 'z':
    if num in vowel:
     print(f"The enter alphabet {num} is vowel")
    elif num not in vowel:
     print(f"The enter alphabet {num} is consonant")
    else:
        print("enter the alphabet only")