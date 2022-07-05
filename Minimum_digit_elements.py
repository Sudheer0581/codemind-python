n=int(input())
arr=list(map(int,input().split()))
m=100
c=0
for i in arr:
    if(len(str(i))<m):
        m=len(str(i))
for i in arr:
    if(len(str(i))==m):
        c+=1
print(c)