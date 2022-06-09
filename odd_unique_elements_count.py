n=int(input())
arr=list(map(int,input().strip().split()))
res=[]
c=0
for i in arr:
    if i not in res and i%2!=0:
        res.append(i)
        c+=1
print(c)
