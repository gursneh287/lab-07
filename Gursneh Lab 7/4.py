N = (input('enter:'))
revN =""
for i in N:
    revN = i+revN
if N == revN:
    print('string is palindrome')
else:
    print('string is not palindrome')     