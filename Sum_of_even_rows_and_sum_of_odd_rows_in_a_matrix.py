r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))
    l.append(arr)
se=so=0
for i in range(r):
    for j in range(c):
        if(i%2==0):
            se+=l[i][j]
        else:
            so+=l[i][j]
print(se,so)