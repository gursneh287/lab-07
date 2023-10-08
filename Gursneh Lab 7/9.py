S=str(input("Enter a string:"))
alphabet="abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    if char not in S.lower():
        print("Not Pangram")
        break
else:
    print("Pangram")
