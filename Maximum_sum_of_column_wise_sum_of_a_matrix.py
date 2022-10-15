r,c=map(int,input().split())
l=[]
col=[]
s=0
for i in range(r):
    arr=list(map(int,input().split()))
    l.append(arr)
for i in range(c):
    for j in range(r):
        s+=l[j][i]
    col.append(s)
    s=0
print(max(col))