a,b=map(int,input().split())
a=list(map(int,input().strip().split()))
a1=set(a)
b=list(map(int,input().strip().split()))
b1=set(b)
c=0
for i in a1:
    if i not in b1:
        c+=1
for i in b1:
    if i not in a1:
        c+=1
print(c)
