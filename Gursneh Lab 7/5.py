P = input('enter para:')
alphabets,digits,special,upp,low=0
for i in range(len(P)):
    if P[i].isalpha():
        alphabets=alphabets+1
        if P[i].isupper():
            upp=upp+1
        elif P[i].islower():
            low=low+1
    elif P[i].isdigit():
        digits=digits+1
    elif P[i]==" " or P[i]=="\n" or P[i]=="\t":
        special=special+1
print(f'Alphabets:{alphabets}')
print(f'Digits:{digits}')
print(f'Special Characters:{special}')
print(f'Upper Case:{upp}')
print(f'Lower Case:{low}')
