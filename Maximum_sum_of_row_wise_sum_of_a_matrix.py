r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))[:c]
    l.append(arr)
max=0
s=0
for i in range(r):
    for j in range(c):
        s=s+l[i][j]
    if(s>max):
        max=s
    s=0
print(max)