def primes(n):
    if(n==1):
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    return True
n=int(input())
arr=list(map(int,input().split()))[:n]
#print(arr)
mi=arr.index(min(arr))
ma=arr.index(max(arr))
c=0
if(mi<ma):
    for i in range(mi,ma+1):
        if primes(arr[i]):
            c+=1
    print(c)
else:
    for i in range(ma,mi+1):
        if primes(arr[i]):
            c+=1
    print(c)