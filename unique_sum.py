n=int(input())
arr=list(map(int,input().strip().split()))
res=[]
for i in arr:
    if i not in res:
        res.append(i)
res=sum(res)
print(str(res))
