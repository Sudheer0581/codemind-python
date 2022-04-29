n=int(input())
count=0
f=0
if(n==1):
    n=2
for i in range(2,n):
    if(n%i==0):
        f=1
        break
if(f==0):
    print("prime")
else:
    print("not a prime")
    