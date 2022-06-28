n=int(input())
arr=list(map(int,input().strip().split()))
for i in range(n):
    if arr[i]==0:
        print(arr[i],end=' ')
for i in range(n):
    if arr[i]==1:
        print(arr[i],end=' ')