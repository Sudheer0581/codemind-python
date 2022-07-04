n=int(input())
arr=list(map(int,input().strip().split()))
#print(arr)
l=[]
for i in arr:
    if i==arr.count(i):
        l.append(i)
        arr.remove(i)
if(len(l)==0):
    print("-1")
else:
    print(min(l),max(l))