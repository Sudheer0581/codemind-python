n=int(input())
arr=list(map(int,input().strip().split()))
c=0
for i in range(1,n-1):
    if arr[i-1]%2==0 and arr[i+1]%2!=0 or arr[i-1]%2!=0 and arr[i+1]%2==0:
        c+=1
if(arr[n-2]%2==0 and arr[0]%2!=0 or arr[n-2]%2!=0 and arr[0]%2==0):
    c+=1
if(arr[n-1]%2==0 and arr[1]%2!=0 or arr[n-1]%2!=0 and arr[1]%2==0):
    c+=1
print(c)