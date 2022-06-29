n=int(input())
arr=list(map(int,input().strip().split()))
f=0
l=[]
for i in arr:
    if arr.count(i)==i and i not in l:
        l.append(i)
        f=1
if f==1:
    print(*l)
else:
    print('-1')