n=input()
c=0
s=0
f=0
d=0
for i in n:
    if i in 'aeiou':
        c+=1
    elif(i==" "):
        s+=1
    elif(i.isdigit()):
        f+=1
    else:
        d+=1 #conso
print("Vowels:",c)
print("Consonants:",d)
print("Digits:",f)
print("White spaces:",s)
