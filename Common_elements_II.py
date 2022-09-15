n,m=map(int,input().split())
a=list(map(int,input().strip().split()))
k=[]
for i in a:
    if i not in k:
        k.append(i)
b=list(map(int,input().strip().split()))
q=[]
for i in b:
    if i not in q:
        q.append(i)
l=[]
for i in k:
    if i not in q:
        l.append(i)
for i in q:
    if i not in k:
        l.append(i)
print(*l)