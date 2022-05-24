n,m=map(int,input().split())
arr=list(map(int,input().strip().split()))[:n]
s=0
for i in arr:
    if(i<0):
        i=i*-1
    p=str(i)
    if(len(p)==m):
        s+=1
print(s)