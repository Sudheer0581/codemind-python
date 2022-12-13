n=int(input())
for i in range(1,n):
    t=2**i
    if(t<=n):
        k=t        
    else:
        z=t
        break
if(abs(n-k)<abs(n-z)):
    print(abs(n-k))
elif(abs(n-k)>abs(n-z)):
    print(abs(n-z))
else:
    print("0")