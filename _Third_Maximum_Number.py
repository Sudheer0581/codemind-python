n=int(input())
arr=list(map(int,input().strip().split()))
s=[]
for i in arr:
    if i in arr and i not in s:
        s.append(i)
l=[]
if len(s)==1:
    print(min(s))
if len(s)==2:
    x=max(s)
    print(x)
if len(s)>=3:
    for i in range(3):
        l.append(max(s))
        s.remove(max(s))
print(min(l))
