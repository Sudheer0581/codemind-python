n=int(input())
arr=list(map(int,input().strip().split()))[:n]
for i in range(n-1,-1,-1):
    if arr[i]%2!=0:
        print(i)
        break