n=int(input())
l=[]
for i in range(n):
    arr=list(map(int,input().split()))
    l.append(arr)
pd=0
sd=0
for i in range(n):
    for j in range(n):
        if i==j:
            pd+=l[i][j]
        if i==(n-1)-j:
            sd+=l[i][j]
print("Principal Diagonal:"+str(pd))
print("Secondary Diagonal:"+str(sd))