n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    #print(b)
    arr=list(map(int,input().strip().split()))
    #print(arr)
    for j in range(b):
        f=arr[-1]
        arr.insert(0,f)
        arr.pop()
    print(*arr)