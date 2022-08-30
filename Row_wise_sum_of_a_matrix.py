r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))[:c]
    l.append(arr)
    #print(l)
s=0
for i in range(r):
    for j in range(c):
        s=s+l[i][j]
    print(s,end=' ')
    s=0