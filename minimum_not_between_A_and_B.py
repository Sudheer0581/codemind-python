n=int(input())
arr=list(map(int,input().strip().split()))
a,b=map(int,input().split())
l=[]
f=0
for i in arr:
    if i<a or i>b:
        l.append(i)
        f=1
if f==0:
    print("-1")
else:
    print(min(l))