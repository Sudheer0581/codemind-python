n=input()
q=n.lower()
#print(n)
v=0
c=0
d=0
w=0
for i in q:
    if i in 'aeiou':
        v+=1
    if i in 'tqwrypsdfghjklzxcvbnm':
        #print(i)
        c+=1
    if i in '1234567890':
        d+=1
    if i in " ":
        w+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',w)