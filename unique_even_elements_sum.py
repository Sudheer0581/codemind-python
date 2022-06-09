n=int(input())
arr=list(map(int,input().strip().split()))
res=[]
for i in arr:
    if i not in res and i%2==0:
        res.append(i)
res=sum(res)
print(str(res))