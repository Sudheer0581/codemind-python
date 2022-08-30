r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))[:c]
    l.append(arr)
s=0
for i in range(r):
    for j in range(c):
        if(i==0 or j==0 or i==r-1 or j==c-1):
            continue
        s=s+l[i][j]
print(s)