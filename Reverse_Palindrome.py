def palin(n):
    q=str(n)
    if(q==q[::-1]):
        return True
    else:
        return False
n=int(input())
while(True):
    q=str(n)
    r=q[::-1]
    s=n+int(r)
    if(palin(s)):
        print(s)
        break
    n=s