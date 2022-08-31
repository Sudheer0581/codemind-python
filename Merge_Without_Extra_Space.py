x=int(input())
for i in range(x):
    n,m=map(int,input().split())
    arr1=list(map(int,input().strip().split()))
    arr2=list(map(int,input().strip().split()))
    s=arr1+arr2
    z=sorted(s)
    print(*z)