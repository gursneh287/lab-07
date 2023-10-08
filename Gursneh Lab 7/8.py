S=str(input("enter a sentence:"))
word=str(input("enter a word:"))

c=0
for i in S.split():
    if i==word:
        c=c+1
print(f'Number of times {word} occurs in {S} is {c}')

print(f'Number of times {word} occurs in {S} is {S.count(word)}')
