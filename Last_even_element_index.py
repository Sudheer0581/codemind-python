n=int(input())
a=list(map(int,input().strip().split()))[:n]
for i in range(n):
    if(a[i]%2==0):
        j=i
print(j)