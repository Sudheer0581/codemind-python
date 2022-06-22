n=int(input())
arr=list(map(int,input().strip().split()))
l=[]
f=0
for i in arr:
    if i==arr.count(i) and i not in l:
        l.append(i)
        f=1
if f==1:
    print(min(l),max(l))
else:
    print("-1")