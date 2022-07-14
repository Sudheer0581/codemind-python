n=input()
s=n.split()
l=[]
c=0
for i in s:
    for j in i:
        if(j in 'aeiou'):
            c+=1
    l.append(c)
    c=0
print(min(l))