n=int(input())
arr=list(map(int,input().strip().split()))
#print(arr)
lo=[]
le=[]
l=[]
for i in arr:
    if(i%2==0):
        le.append(i)
    else:
        lo.append(i)
for i in range(min(len(le),len(lo))):
    l.append(lo[i])
    l.append(le[i])
    arr.remove(lo[i])
    arr.remove(le[i])
l.extend(arr)
if(len(l)%2==0):
    print(*l)
else:
    l.append(0)
    print(*l)
    