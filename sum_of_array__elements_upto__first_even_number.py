n=int(input())
arr=list(map(int,input().strip().split()))[:n]
s=0
for i in range(len(arr)):
    if(arr[i]%2==0):
        break
    s=s+arr[i]
print(s)