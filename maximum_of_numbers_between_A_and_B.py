n=int(input())
arr=list(map(int,input().strip().split()))
a,b=map(int,input().strip().split())
l=[]
f=0
for i in range(a,b+1):
    if(i in arr):
        l.append(i)
        f=1
if f==1:
    print(max(l))
else:
    print("-1")