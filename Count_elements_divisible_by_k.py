a,b=map(int,input().split())
arr=list(map(int,input().strip().split()))
c=0
for i in arr:
    if i%b==0:
        c+=1
print(c)