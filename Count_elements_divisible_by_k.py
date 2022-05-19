n,m=map(int,input().strip().split())
arr=list(map(int,input().strip().split()))[:n]
c=0
for i in range(n):
    if(arr[i]%m==0):
        c+=1
print(c)