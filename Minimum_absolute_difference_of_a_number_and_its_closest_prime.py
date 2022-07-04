def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
temp=n
t1=n
while(True):
    if(prime(n)):
        s=n
        break
    n+=1
while(True):
    if(prime(temp)):
        f=temp
        break
    temp=temp-1
if(s-t1<t1-temp):
    print(s-t1)
else:
    print(t1-temp)