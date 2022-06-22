n=input()
s=" "
c=0
for i in n:
    if i in n.lower() and i not in s:
        c+=1
print(c)