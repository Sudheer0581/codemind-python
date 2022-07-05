n=int(input())
arr=list(map(int,input().strip().split()))
m=0
c=0
for i in arr:
    if len(str(i))>m:
        m=len(str(i))
for i in arr:
    if(len(str(i))==m):
        print(i,end=" ")