n=int(input())
arr=list(map(int,input().strip().split()))
l=[]
c=0
for i in arr:
    #print(arr.count(i))
    if i==arr.count(i) and i not in l:
        l.append(i)
        c+=1
print(c)