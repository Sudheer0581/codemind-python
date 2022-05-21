import math
def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True

n=int(input())
for i in range(n):
    a=int(input())
    temp=a
    t1=a
    while(True):
        if(prime(a)):
            k=a
            break
        a+=1
    while(True):
        if(prime(temp)):
            f=temp
            break
        else:
            temp=temp-1
    if((a-t1)<(t1-f)):
        print(a)
    else:
        print(f)
    