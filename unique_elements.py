n=int(input())
arr=list(map(int,input().strip().split()))
l=[]
c=0
for i in range(n):
    for j in range(n):
        if arr[i]==arr[j] and arr[i] not in l:
            c+=1
    if c>=1:
        l.append(arr[i])
    c=0
for i in range(len(l)):
    print(l[i],end=' ')
    
    