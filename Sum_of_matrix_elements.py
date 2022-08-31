n=int(input())
m=int(input())
l=[]
for i in range(n):
    arr=list(map(int,input().strip().split()))
    l.append(arr)
s=0
for i in range(n):
    for j in range(m):
        s=s+l[i][j]
print(s)