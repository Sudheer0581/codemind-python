n=int(input())
arr=list(map(int,input().strip().split()))
a,b=map(int,input().strip().split())
l=[]
s=0
for i in range(a,b+1):
    if(i in arr):
        l.append(i)
        s=s+i
print(s)