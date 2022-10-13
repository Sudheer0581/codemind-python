def prime(n):
    x=0
    for j in range(1,n+1):
        if n%j==0:
            x+=1
    if x==2:
        return True
n=int(input())
c=0
c1=0
if prime(n)==True:
    temp=n
    while(temp>0):
        r=temp%10
        c+=1
        if prime(r)==True:
            c1+=1
        temp//=10
    if c1==c:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")