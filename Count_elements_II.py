m,n=map(int,input().split())
arr1=list(map(int,input().strip().split()))
a1=set(arr1)
arr2=list(map(int,input().strip().split()))
a2=set(arr2)
c=0
for i in a1:
    if i not in a2:
        c+=1
for i in a2:
    if i not in a1:
        c+=1
print(c)