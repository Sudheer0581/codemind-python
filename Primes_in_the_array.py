def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
arr=list(map(int,input().strip().split()))[:n]
c=0
s=0
for i in range(n):
    if(prime(arr[i]) and arr[i]!=1):
        c+=1
print(c)