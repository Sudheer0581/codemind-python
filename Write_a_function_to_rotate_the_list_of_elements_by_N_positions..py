n=int(input())
arr=list(map(int,input().split()))
m=int(input())
for i in range(m):
    arr.insert(0,arr[-1])
    arr.pop()
print(*arr)