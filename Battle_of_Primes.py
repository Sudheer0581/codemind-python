def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
m=int(input())
p=m+n
c=0

for i in range(1,10):
    p=p+1
    if(prime(p)):
        c=i
        break
print(c)