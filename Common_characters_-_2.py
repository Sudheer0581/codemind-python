a=input()
a=a.lower()
a=a.split()
k=""
l=str(a[0])
for j in l:
    c=0
    for x in range(1,len(a)):
        a[x]=str(a[x])
        if j in a[x]:
            c+=1
    if c==len(a)-1:
        k+=j
print(len(k))