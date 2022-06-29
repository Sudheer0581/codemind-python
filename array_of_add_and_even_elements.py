n=int(input())
arr=list(map(int,input().strip().split()))
l=[]
for i in arr:
    if i%2!=0:
        l.append(i)
for i in arr:
    if i%2==0:
        l.append(i)
print(*l)