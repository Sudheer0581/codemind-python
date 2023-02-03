a,b=map(int,input().split())
ar=list(map(int,input().split()))
#print(a,b)
#print(ar)
l=[]
k=[]
for i in range(b):
    l.append(ar[i])
for i in range(b,a):
    k.append(ar[i])
print(*(k+l))