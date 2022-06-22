n=int(input())
arr=list(map(int,input().strip().split()))
m=int(input())
l=[]
f=0
for i in arr:
    if arr.count(i)==m and i not in l:
        l.append(i)
        f=1
if f==1:
    print(*l)
else:
    print("-1")
        