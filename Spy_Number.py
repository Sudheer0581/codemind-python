n=int(input())
s=0
p=1
while(n):
    r=n%10
    s=s+r
    p=p*r
    n=n//10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")