n=int(input())
arr=list(map(int,input().strip().split()))
l=[]
for i in arr:
    if i in arr and i not in l:
        l.append(i)
print(*l)
        