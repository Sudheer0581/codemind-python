n=int(input())
arr=list(map(int,input().strip().split()))
k=int(input())
s=0
for i in range(n):
    if(arr[i]<=k):
        s=s+arr[i]
print(s)