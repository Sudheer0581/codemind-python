n=int(input())
arr=list(map(int,input().strip().split()))
#print(arr)
l=[]
a,b=map(int,input().split())
for i in range(n):
    if(arr[i]>=a and arr[i]<=b):
        l.append(arr[i])
if(len(l)==0):
    print("-1")
else:
    print(min(l))