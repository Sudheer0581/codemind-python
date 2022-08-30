r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))
    l.append(arr)
s=0
for i in range(c):
    for j in range(r):
        s=s+l[j][i]
    print(s,end=' ')
    s=0