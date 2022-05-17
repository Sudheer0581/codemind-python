n=int(input())
arr=list(map(int,input().strip().split()))[:n]
a,b=map(int,input().strip().split())
max=0
l=[]
for i in range(n):
    if(arr[i]>=a and arr[i]<=b):
        continue
    l.append(arr[i])
if(len(l)==0):
    print(-1)
else:
    max=l[0]
    for i in range(1,len(l)):
        if(l[i]>max):
            max=l[i]
    print(max)
   