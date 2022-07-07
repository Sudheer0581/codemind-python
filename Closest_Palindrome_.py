def palin(n):
    q=str(n)
    s=q[::-1]
    if(s==q):
        return True
    else:
        return False
n=int(input())
q=n+1
temp=n-1
t1=n
while(True):
    if(palin(q)):
        s=q
        break
    q=q+1
while(True):
    if(palin(temp)):
        k=temp
        break
    temp=temp-1
if(s-t1==t1-k):
    print(k,s)
else:
    if(s-t1>t1-k):
        print(k)
    else:
        print(s)


        
    