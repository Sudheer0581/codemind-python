n=input()
a=n.lower()
c=0
for i in a:
    if i!=' ':
        if a.count(i)==1:
            c+=1
print(c)