def count(n):
    q=str(n)
    return len(q)
n=int(input())
arr=list(map(int,input().strip().split()))
max=0
c=0
for i in arr:
    b=count(i)
    if(b>max):
        max=b
for i in arr:
    if(len(str(i))==max):
        print(i,end=" ")
    