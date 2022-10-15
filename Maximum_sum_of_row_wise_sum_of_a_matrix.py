r,c=map(int,input().split())
l=[]
col=[]
s=0
for i in range(r):
    arr=list(map(int,input().split()))
    l.append(arr)
for i in range(r):
    for j in range(c):
        s+=l[i][j]
    col.append(s)
    s=0
print(max(col))