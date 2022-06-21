n=int(input())
arr=list(map(int,input().strip().split()))[:n]
print(*arr[n:n//2-1:-1],end=" ")
print(*arr[:n//2])
    