n=int(input())
a,b=0,1
f=0
if(n==1 or n==0):
    print(True)
for i in range(1,n-1):
    c=a+b
    if(c==n):
        f=1
        break
    a=b
    b=c
if(f==1):
    print(True)
else:
    print(False)