n=input()
n=n.lower()
n=n.split()
k=''
l=str(n[0])
for j in l:
    c=0
    for x in range(1,len(n)):
        n[x]=str(n[x])
        if j in n[x]:
            c+=1
    if c==len(n)-1:
        k+=j
if len(k)==0:
    print(-1)
else:
    print(k)