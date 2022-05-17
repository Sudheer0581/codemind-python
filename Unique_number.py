n=int(input())
temp=n
count=0
c=0
f=0
temp2=n
while(n):
    temp=temp2
    count+=1
    c=0
    r=n%10
    while(temp):
        r1=temp%10
        if(r1==r):
            c+=1
        temp//=10
    if(c==1):
        f+=1
    n//=10
if(f==count):
    print("Unique Number")
else:
    print("Not Unique Number")