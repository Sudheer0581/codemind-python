n=int(input())
f=0
arr=list(map(int,input().strip().split()))[:n]
for i in range(0,n):
    if(arr[i]%2==0):
        f+=1
if(f==len(arr)):
    print('True')
else:
    print('False')