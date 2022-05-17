n=int(input())
arr=list(map(int,input().strip().split()))[:n]
c=0
s=0
for i in range(n):
    s=s+arr[i]
a=s//n
for i in range(n):
    if arr[i]<=a:
        c+=1
print(c)