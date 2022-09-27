n=int(input())
a=list(map(int,input().strip().split()))
x=sorted(a)
z=x[::-1]
s=len(z)
if s%2!=0:
    for i in range(0,s-2,2):
        k=z[i]
        z[i]=z[i+1]
        z[i+1]=k
    print(*z)
else:
    for i in range(0,s-1,2):
        k=z[i]
        z[i]=z[i+1]
        z[i+1]=k
    print(*z)