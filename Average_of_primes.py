def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
arr=list(map(int,input().strip().split()))
s=0
c=0
for i in range(n):
    if prime(arr[i]) and arr[i]!=1:
        s=s+arr[i]
        c+=1
avg=(s/c)
print("{:.2f}".format(avg))