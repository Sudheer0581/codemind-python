n=int(input())
s=0
temp=n*n
while(temp!=0):
    r=temp%10
    s=s+r
    temp=temp//10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")