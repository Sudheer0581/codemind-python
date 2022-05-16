n=int(input())
arr=list(map(int,input().strip().split()))[:n]
l=[]
a,b=map(int,input().strip().split())
for i in range(0,n):
    if arr[i]>=a and arr[i]<=b:
        continue
    l.append(arr[i])
if(len(l)==0):
    print("-1")
else:
    for i in range(len(l)):
        print(l[i],end=" ")