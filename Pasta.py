n,m=map(int,input().split())
a=list(map(int,input().split()))[:n]
l=list(map(int,input().split()))[:m]
c=0
for i in l:
    if i in a:
        a.remove(i)
        c+=1
if c==len(l):
    print("Yes")
else:
    print("No")