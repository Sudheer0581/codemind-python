r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))
    l.append(arr)
s=0
for i in range(r):
    for j in range(c):
        s+=l[i][j]
print(s)