n=int(input())
arr=list(map(int,input().strip().split()))
for i in range(n):
    if arr[i]%2!=0:
        j=i
print(j)