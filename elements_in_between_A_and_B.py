n=int(input())
arr=list(map(int,input().strip().split()))
#print(arr)
a,b=map(int,input().split())
#print(a,b)
f=0
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        print(arr[i],end=' ')
        f=1
if f==0:
    print("-1")
