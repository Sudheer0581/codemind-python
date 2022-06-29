n=int(input())
arr=list(map(int,input().strip().split()))
c=0
l=[]
for i in arr:
    if i==arr.count(i) and i not in l:
        l.append(i)
        c+=1
print(c)