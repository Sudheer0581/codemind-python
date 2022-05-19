n=int(input())
arr=list(map(int,input().strip().split()))[:n]
c=0
f=0
for i in range(n):
    if(arr[i]%2==0):
        f+=1
        if(i%2==0):
            c+=1
if(c==f):
    print("True")
else:
    print("False")
