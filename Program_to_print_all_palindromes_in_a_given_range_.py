def palin(n):
    q=str(n)
    if(q==q[::-1]):
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if palin(i):
        print(i,end=' ')
    