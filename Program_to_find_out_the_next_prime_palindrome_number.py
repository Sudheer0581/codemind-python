def prime(n):
    for i in range(2,n//2+1):
        if(n%i)==0:
            return False
    else:
        return True
def palin(n):
    temp=n
    rev=0
    while(temp>0):
        r=temp%10
        rev=rev*10+r
        temp//=10
    if(rev==n):
        return n
n=int(input())
temp=n+1
while(True):
    if(palin(temp) and prime(temp)):
        print(temp)
        break
    temp+=1