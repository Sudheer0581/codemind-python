n=int(input())
f=0
arr=[]
for i in range(2,n//2+1):
    c=0
    for j in range(2,i//2+1):
        if(i%j==0):
            c=1
            break
    if(c==0):
        arr.append(i)
for k in range(0,len(arr)):
    for j in range(k+1,len(arr)): #1 2
        if(arr[k]*arr[j]==n):
            f=1
            p=arr[k]
            q=arr[j]
            break
if(f==1):
    print(p,q)
else:
    print("-1")
        