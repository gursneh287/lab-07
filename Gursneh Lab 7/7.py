s=str(input("Enter a string:"))
p=""
for char in s:
    if char not in p:
        p=p+char
print(f'Original string is: {s}')
print(f'New string without duplicate characters is: {p}')

