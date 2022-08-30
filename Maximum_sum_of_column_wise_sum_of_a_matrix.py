r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))[:c]
    l.append(arr)
max=0
s=0
for i in range(c):
    for j in range(r):
        s=s+l[j][i]
    if(s>max):
       max=s
    s=0
print(max)