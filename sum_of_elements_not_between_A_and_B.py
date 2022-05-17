n=int(input())
arr=list(map(int,input().strip().split()))[:n]
a,b=map(int,input().strip().split())
s=0
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        continue
    s=s+arr[i]
print(s)